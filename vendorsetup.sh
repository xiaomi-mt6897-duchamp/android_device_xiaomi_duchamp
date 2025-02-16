# 1. Apply Git Changes (Source Modification)
echo "Applying source modifications..."

# UDFPS Patch for frameworks/base
echo "Fetching and applying UDFPS patch for frameworks/base..."
cd frameworks/base
git fetch https://github.com/xiaomi-mt6897-duchamp/PixelOS_frameworks_base
git cherry-pick 6e465226c80db0395340605b81ec9f910b566817 97b618cb948f36ad75515963b41dd2304a59524a 
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

# Nuke refresh rate selector
echo "Nuking refresh rate selector so no one mess with it"
cd  packages/apps/Settings
git fetch https://github.com/xiaomi-mt6897-duchamp/android_packages_apps_Settings
git cherry-pick 697a70a15351479b048e17205686a71147b92504
cd ../../../

# Private Keys Setup
echo "Setting up private signing keys..."
git clone https://github.com/zenin1504/private-keys.git /tmp/keys
rm -rf vendor/aosp/signing/keys
mv /tmp/keys vendor/aosp/signing/keys

# V4A
git clone https://github.com/xiaomi-mt6897-duchamp/packages_apps_ViPER4AndroidFX.git -b v4a packages/apps/ViPER4AndroidFX
echo "Removing accidentally clone..."
rm -rf packages/yapps/ViPER4AndroidFX

echo "All operations completed successfully!"
