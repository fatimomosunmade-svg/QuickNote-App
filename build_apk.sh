#!/bin/bash
echo "=== Setting up Android SDK ==="
yes | sdkmanager --licenses
sdkmanager "platform-tools" "platforms;android-31" "build-tools;30.0.3" "ndk;23.1.7779620"

echo "=== Building APK with Buildozer ==="
cd app
buildozer -v android debug

echo "=== Build Complete ==="
ls -la bin/
