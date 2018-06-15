#!/usr/bin/env python3
# coding: utf8

from resources import DslamHuawei
from resources import Settings

command_list = [
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 1024 32 920 name auto_1-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 2048 32 920 name auto_2-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 3072 32 920 name auto_3-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 4096 32 920 name auto_4-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 5120 32 920 name auto_5-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 6144 32 920 name auto_6-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 7168 32 920 name auto_7-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 8192 32 920 name auto_8-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 9216 32 920 name auto_9-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 10240 32 920 name auto_10-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 11264 32 920 name auto_11-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 12288 32 920 name auto_12-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 13312 32 920 name auto_13-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 14336 32 920 name auto_14-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 15360 32 920 name auto_15-1-9',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 9 0 31 6 0 31 6 12 3 9 shifttime 10 10 10  10 rate 32 16384 32 920 name auto_16-1-9'
]

for host in Settings.hosts:
    if host[1] == '5600':
        dslam = DslamHuawei.DslamHuawei5600(host[0], Settings.login_5600, Settings.password_5600)
    elif host[1] == '5616':
        dslam = DslamHuawei.DslamHuawei5616(host[0], Settings.login_5616, Settings.password_5616)
    dslam.execute_command('config', short=True)
    for command in command_list:
        out = dslam.execute_command(command)
        print(dslam.hostname, ': ',out)
    del dslam
