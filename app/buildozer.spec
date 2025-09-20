[app]

# (str) Title of your application
title = QuickNote

# (str) Package name
package.name = quicknote

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bigdev

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.1.0,kivymd==1.1.1,openssl,pyopenssl

# (str) Icon of the application
#icon.filename = assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 23

# (str) Android NDK version to use
#android.ndk = 23b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# Fix for the "Aidl not found" error
android.build_tools_version = 34.0.0
