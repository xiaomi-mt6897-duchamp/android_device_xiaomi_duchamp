# 1. Apply Git Changes (Source Modification)
echo "Applying source modifications..."

# UDFPS Patch for frameworks/base
echo "Fetching and applying UDFPS patch for frameworks/base..."
cd frameworks/base
git fetch https://github.com/xiaomi-mt6897-duchamp/frameworks_base
git cherry-pick 1338dbc45b052a74e0a6fe5f1236fac5836aaef1 41c5fdec468450b87378c6ccddd5aafb2dcb6939
cd ../../

# Hardware Compatibility Fixes
echo "Fetching and applying hardware compatibility fixes for hardware/lineage/compat..."
cd hardware/lineage/compat
git fetch https://github.com/xiaomi-mt6897-duchamp/android_hardware_lineage_compat
git cherry-pick 9a046ea7e5899adc38ab04fe24eb34859fe4d779
cd ../../../

# Hardware Legacy Modifications
echo "Fetching and applying fixes for hardware/libhardware_legacy..."
cd hardware/libhardware_legacy
git fetch https://android.googlesource.com/platform/hardware/libhardware_legacy 54bb5d03278152e696c7bff4607278790ac73057
git cherry-pick 54bb5d03278152e696c7bff4607278790ac73057
cd ../../

# Private Keys Setup
echo "Setting up private signing keys..."
git clone https://github.com/zenin1504/private-keys.git /tmp/keys
rm -rf vendor/derp/signing/keys
mv /tmp/keys vendor/derp/signing/keys

# V4A
git clone https://github.com/xiaomi-mt6897-duchamp/packages_apps_ViPER4AndroidFX.git -b v4a packages/apps/ViPER4AndroidFX
echo "Removing accidentally clone..."
rm -rf packages/yapps/ViPER4AndroidFX

echo "All operations completed successfully!"
