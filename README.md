# XAPK creation tool

This XAPK creation tool will create an XAPK file from a folder containing an APK file and an OBB file. The `icon.png` and `manifest.json` files are generated from the APK file.

## Usage

```
xapktool.py <apk_obb_directory>
```

## Notes

* The tool expects a directory with a single apk and single obb file.
* There is no check to ensure that the OBB and APK are from the same application. There is also no check for cases where there is no obb file.
** Probably should enforce that obb files are correctly named (`[main|patch].<expansion-version>.<package-name>.obb`), as per https://developer.android.com/google/play/expansion-files#GettingFilenames

## Authors

* XAPK creation tool: Shii Kayano
* Androguard + tools: Anthony Desnos (desnos at t0t0.fr).
* DAD (DAD is A Decompiler): Geoffroy Gueguen (geoffroy dot gueguen at gmail dot com)

## Licenses

### XAPK creation tool

Copyright (C) 2020, Shii Kayano (bryghtshadow at gmail dot com)
All rights reserved

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### Androguard

Copyright (C) 2012 - 2016, Anthony Desnos (desnos at t0t0.fr)
All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### DAD

Copyright (C) 2012 - 2016, Geoffroy Gueguen (geoffroy dot gueguen at gmail dot com)
All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.