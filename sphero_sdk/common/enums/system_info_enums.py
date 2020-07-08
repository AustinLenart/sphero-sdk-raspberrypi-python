#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          07/08/2020 @ 22:29:07.245249 (UTC)

from enum import IntEnum


__all__ = ['ConfigBlockWriteCodesEnum',
           'DeviceModesEnum',
           'ApplicationIndexesEnum',
           'SosMessagesEnum']


class CommandsEnum(IntEnum): 
    get_main_application_version = 0x00
    get_bootloader_version = 0x01
    get_board_revision = 0x03
    get_mac_address = 0x06
    get_stats_id = 0x13
    get_processor_name = 0x1F
    get_sku = 0x38
    get_core_up_time_in_milliseconds = 0x39


class ConfigBlockWriteCodesEnum(IntEnum):
    CB_SUCCESS = 0
    CB_BUSY = 1
    CB_FS_ERROR = 2


class DeviceModesEnum(IntEnum):
    factory_mode = 0
    user_play_test_mode = 1
    user_out_of_box_mode = 2
    user_full_mode = 3


class ApplicationIndexesEnum(IntEnum):
    bootloader = 0
    main_application = 1


class SosMessagesEnum(IntEnum):
    unknown = 0
    subprocessor_crashed = 1
