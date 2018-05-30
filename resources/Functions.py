# coding: utf8

import MySQLdb
import datetime
import time
import re
import os
from resources import DslamHuawei
from resources import Settings

DslamHuawei.LOGGING = True

def get_sql_data():
    connect = MySQLdb.connect(host=Settings.db_host, user=Settings.db_user, password=Settings.db_password, db=Settings.db_name, charset='utf8')
    cursor = connect.cursor()    
    command = '''
    SELECT DISTINCT dd.hostname, dd.board, dd.port, TRUNCATE(AVG(dd.max_dw_rate)/1000, 0), TRUNCATE(ad.tariff/1000, 0), ad.tv
    FROM data_dsl dd INNER JOIN abon_dsl ad
     ON dd.hostname = ad.hostname
     AND dd.board = ad.board
     AND dd.port = ad.port
    WHERE CAST(dd.datetime  as DATE) = DATE_ADD(CURRENT_DATE(), INTERVAL -1 DAY)
     AND ad.area LIKE '%Петровск%'
    GROUP BY dd.hostname, dd.board, dd.port
    HAVING AVG(max_dw_rate) IS NOT NULL
    ORDER BY dd.hostname, dd.board, dd.port
    '''
    cursor.execute(command)
    raw_data = cursor.fetchall()
    connect.close()
    result = {}
    for data in raw_data:
        result['{}/{}/{}'.format(data[0], data[1], data[2])] = {'speed': data[3], 'tariff': data[4], 'tv': data[5]}
    return result

def choose_profile(speed, tariff, tv):
    # Добавляю 6Мб если есть ТВ
    if tariff is not None and tv == 'yes':
        tariff += 6
    # Подбираю профиль
    if tariff is None:
        result = speed - 2
    elif tariff + 3 <= speed:
        result = tariff + 1
    else:
        result = speed - 2
    if result <= 0:
        return False
    elif result > 16:
        return 16
    else:
        return int(result)

def connect_dslam(host):
    ip = host[0]
    model = host[1]
    
    if model == '5600':
        dslam = DslamHuawei.DslamHuawei5600(ip, Settings.login_5600, Settings.password_5600)
    elif model == '5616':
        dslam = DslamHuawei.DslamHuawei5616(ip, Settings.login_5616, Settings.password_5616)
        
    dslam.program_profiles = {}
    re_string = r'^petr_(\d+)-\d+-\d+$'
    for profile in dslam.adsl_line_profile:
        work_profile = re.search(re_string, dslam.adsl_line_profile[profile]['profile_name'])
        if work_profile:
            dslam.program_profiles[int(work_profile.group(1))] = profile   
    return dslam
    

def run(arguments):
    host = arguments[0]
    data = arguments[1]
    
    try:
        dslam = connect_dslam(host)
    except Exception as ex:
        print(ex)
        return False
    hostname = dslam.hostname
    if not os.path.exists('profile_logs'):
        os.mkdir('profile_logs')
        
    print('Обработка {}'.format(hostname))  
    with open('profile_logs{}{}.txt'.format(os.sep, hostname), 'w') as log_file:
        log_file.write('--- {} ---\n'.format(datetime.datetime.now().strftime('%d-%m-%y %H:%M')))   
        for board in dslam.boards:
            current_profiles = dslam.get_adsl_line_profile_board(board)
            for port in range(0, dslam.ports):
                key = '{}/{}/{}'.format(hostname, board, port)
                if (key not in data) or (key in Settings.black_list):
                    continue
                profile_speed = choose_profile(data[key]['speed'], data[key]['tariff'], data[key]['tv'])
                if profile_speed:
                    if dslam.program_profiles[profile_speed] == current_profiles[port]:
                        log_file.write('{} - менять профиль не нужно (скорость {}, тариф {}, TV {}, профиль {})\n'.format(key, data[key]['speed'], data[key]['tariff'], data[key]['tv'], profile_speed))
                        continue
                    if profile_speed in dslam.program_profiles:
                        log_file.write('{} - скорость {}, тариф {}, TV {}, профиль {}\n'.format(key, data[key]['speed'], data[key]['tariff'], data[key]['tv'], profile_speed))
                        dslam.set_adsl_line_profile_port(board, port, dslam.program_profiles[profile_speed])
                        time.sleep(1)
                    else:
                        log_file.write('{} - не удалось найти профиль, скорость {}, тариф {}, TV {}\n'.format(key, data[key]['speed'], data[key]['tariff'], data[key]['tv']))
                        continue
    print('{} обработан'.format(hostname))
    del dslam
                