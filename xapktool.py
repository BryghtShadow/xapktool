import os
import sys
import json
from pathlib import Path, PurePath
import tempfile
import shutil
import zipfile

import androguard
from androguard.core.bytecodes.apk import APK

class XAPK:
    def __init__(self, folder):
        self.folder = Path(folder)
        for x in self.folder.glob('*.apk'):
            self.apk_src = Path(x)
        for x in self.folder.glob('*.obb'):
            self.obb_src = Path(x)
        self.apk = APK(self.apk_src)
        self.manifest = self.make_manifest()
        self.icon = self.apk.get_file(self.apk.get_app_icon())

    def make_manifest(self):
        apk_size = self.apk_src.stat().st_size
        obb_size = self.obb_src.stat().st_size
        total_size = apk_size + obb_size
        filename = self.apk.get_filename()

        manifest = {}
        manifest['xapk_version'] = 1
        manifest['package_name'] = self.apk.get_package()
        manifest['name'] = self.apk.get_app_name()
        # manifest['locales_name'] = {} # TODO
        manifest['version_code'] = self.apk.get_androidversion_code()
        manifest['version_name'] = self.apk.get_androidversion_name()
        manifest['min_sdk_version'] = self.apk.get_min_sdk_version()
        manifest['target_sdk_version'] = self.apk.get_target_sdk_version()
        manifest['permissions'] = self.apk.get_declared_permissions()
        manifest['total_size'] = total_size

        expansion = {}
        expansion['file'] = 'Android/obb/{package_name}/main.{version_code}.{package_name}.obb'.format(**manifest)
        expansion['install_location'] = 'EXTERNAL_STORAGE'
        expansion['install_path'] = 'Android/obb/{package_name}/main.{version_code}.{package_name}.obb'.format(**manifest)
        manifest['expansions'] = [expansion]

        return manifest

    def save(self):
        self.name = '{package_name}_v{version_name}.xapk'.format(**self.manifest)
        zip_path = self.folder.joinpath(self.name)

        zip_dir = tempfile.mkdtemp()
        try:
            print('copying apk to temp directory...')
            apk_name = '{package_name}.apk'.format(**self.manifest)
            apk_src = self.apk_src.resolve()
            apk_dest = PurePath(zip_dir).joinpath(apk_name)
            shutil.copy2(apk_src, apk_dest)
            print('apk: OK')

            print('copying obb to temp directory...')
            obb_name = self.manifest['expansions'][0]['install_path']
            obb_src = self.obb_src.resolve()
            obb_dest = PurePath(zip_dir).joinpath(obb_name)
            os.makedirs(Path(obb_dest).parent, exist_ok=True)
            shutil.copy2(obb_src, obb_dest)
            print('obb: OK')

            print('creating icon in temp directory...')
            icon = self.icon
            icon_dest = PurePath(zip_dir).joinpath('icon.png')
            with open(icon_dest, 'wb') as iconfile:
                iconfile.write(icon)
            print('icon: OK')

            print('creating manifest in temp directory...')
            manifest_dest = PurePath(zip_dir).joinpath('manifest.json')
            with open(manifest_dest, 'w') as manifestfile:
                s = json.dumps(self.manifest, separators=(':',','))
                manifestfile.write(s)
            print('manifest: OK')

            print('creating xapk archive...')
            with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zfd:
                for root, dirs, files in os.walk(zip_dir):
                    for f in files:
                        filename = os.path.join(root, f)
                        zfd.write(filename, os.path.relpath(filename, zip_dir))
            print('xapk: OK')
        finally:
            print('cleaning up temp directory...')
            shutil.rmtree(zip_dir)
            print('cleanup: OK')

def main(args):
    folder = args[0]
    xapk = XAPK(folder)
    xapk.save()

if __name__ == '__main__':
    main(sys.argv[1:])
