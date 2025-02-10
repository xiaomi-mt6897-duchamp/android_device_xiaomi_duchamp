#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/duchamp',
    'hardware/mediatek',
    'hardware/xiaomi',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}-{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('libjpegdecoder',
     'libjpegencoder',
     'libmialgo_aio_seg',
     'libmialgo_utils',
     'libultrahdr',
     'vendor.mediatek.hardware.videotelephony-V1-ndk',
     'vendor.xiaomi.hardware.fingerprintextension-V1-ndk',
     'vendor.xiaomi.hw.touchfeature-V1-ndk'): lib_fixup_vendor_suffix,
    ('libsink',): lib_fixup_remove,
}


blob_fixups: blob_fixups_user_type = {
    'system_ext/priv-app/ImsService/ImsService.apk': blob_fixup()
        .apktool_patch('blob-patches/ImsService.patch'),

    'system_ext/lib64/libsink.so': blob_fixup()
        .add_needed('libaudioclient_shim.so'),

    'odm/bin/hw/vendor.xiaomi.sensor.citsensorservice.aidl': blob_fixup()
        .add_needed('libui_shim.so'),

    'vendor/lib64/c2.dolby.client.so': blob_fixup()
        .add_needed('libshim_codec2_hidl.so'),

    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V2-ndk.so')
        .replace_needed('libalsautils.so', 'libalsautils-v34.so'),

    ('vendor/lib64/mt6897/lib3a.ae.stat.so',
     'vendor/lib64/libarmnn_ndk.mtk.vndk.so'): blob_fixup()
        .add_needed('liblog.so'),

    'vendor/lib64/vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V2-ndk.so'),

    'vendor/bin/hw/mfp-daemon': blob_fixup()
        .replace_needed('android.hardware.biometrics.common-V3-ndk.so', 'android.hardware.biometrics.common-V4-ndk.so')
        .replace_needed('android.hardware.biometrics.fingerprint-V3-ndk.so', 'android.hardware.biometrics.fingerprint-V4-ndk.so'),

    ('vendor/bin/hw/mt6897/android.hardware.graphics.allocator-V2-service-mediatek.mt6897',
     'vendor/lib64/egl/mt6897/libGLES_mali.so',
     'vendor/lib64/hw/mt6897/android.hardware.graphics.allocator-V2-mediatek.so',
     'vendor/lib64/hw/mt6897/android.hardware.graphics.mapper@4.0-impl-mediatek.so',
     'vendor/lib64/hw/mt6897/mapper.mediatek.so',
     'vendor/lib64/libaimemc.so',
     'vendor/lib64/libcodec2_fsr.so',
     'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
     'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
     'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
     'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V2-ndk.so',
     'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V4-ndk.so',
     'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V6-ndk.so'): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V5-ndk.so'),

    'vendor/lib64/mt6897/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V2-ndk.so', 'android.hardware.camera.common-V1-ndk.so'),

    ('vendor/lib64/mt6897/libmtkcam_grallocutils.so',
     'vendor/lib64/libmtkcam_grallocutils_aidlv1helper.so'): blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so')
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V5-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'duchamp',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
