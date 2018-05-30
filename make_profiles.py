#!/usr/bin/env python3
# coding: utf8

from resources import DslamHuawei


#dslam = DslamHuawei.DslamHuawei5600('ip', 'login', 'password')
dslam = DslamHuawei.DslamHuawei5616('ip', 'login', 'password')

command_list = [
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 1024 32 1024 name petr_1-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 2048 32 1024 name petr_2-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 3072 32 1024 name petr_3-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 4096 32 1024 name petr_4-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 5120 32 1024 name petr_5-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 6144 32 1024 name petr_6-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 7168 32 1024 name petr_7-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 8192 32 1024 name petr_8-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 9216 32 1024 name petr_9-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 10240 32 1024 name petr_10-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 11264 32 1024 name petr_11-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 12288 32 1024 name petr_12-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 13312 32 1024 name petr_13-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 14336 32 1024 name petr_14-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 15360 32 1024 name petr_15-1-10',
    'adsl line-profile quickadd basic-para all trellis 1 bitswap 1 1 channel interleaved 6 6 adapt at-runtime snr 10 0 31 10 0 31 3 15 3 15 shifttime 60 60  60 60 rate 32 16384 32 1024 name petr_16-1-10'
]
dslam.execute_command('config', short=True)

for command in command_list:
    out = dslam.execute_command(command)
    print(out)
    

del dslam
