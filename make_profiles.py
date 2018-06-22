#!/usr/bin/env python3
# coding: utf8

from resources import DslamHuawei
from resources import Settings

command_list = [
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 1024 32 896 name petr_1-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 2048 32 896 name petr_2-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 3072 32 896 name petr_3-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 4096 32 896 name petr_4-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 5120 32 896 name petr_5-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 6144 32 896 name petr_6-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 7168 32 896 name petr_7-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 8192 32 896 name petr_8-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 9216 32 896 name petr_9-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 10240 32 896 name petr_10-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 11264 32 896 name petr_11-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 12288 32 896 name petr_12-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 13312 32 896 name petr_13-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 14336 32 896 name petr_14-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 15360 32 896 name petr_15-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 0 0 channel interleaved 6 6 adapt at-startup snr 10 0 31 8 0 31 rate 32 16384 32 896 name petr_16-1-10'
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
