#!/usr/bin/env python3
# coding: utf8

import datetime
import time
import os
from concurrent.futures import ThreadPoolExecutor
from resources import Functions as f
from resources import Settings


def main():
    run_interval = Settings.run_interval * 60 * 60
    
    if not os.path.exists('profile_logs'):
        os.mkdir('profile_logs')    
    
    while True:
        current_time = datetime.datetime.now()
        if 'run_time' in locals():
            if (current_time - run_time).seconds < run_interval:
                time.sleep(600)
                continue
        
        print('Начало работы: {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
        print('\n\nПолучение данных из SQL-базы...')
        sql_data = f.get_sql_data()
        #for data in sql_data:
            #print(data, sql_data[data])
        print('\nДанные для работы получены. Запуск обработки DSLAM...\n')
        
        arguments = [(host, sql_data) for host in Settings.hosts]
        
        with ThreadPoolExecutor(max_workers=Settings.threads) as executor:
            executor.map(f.run, arguments)
        
        print('Завершение работы: {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')))
        run_time = current_time



if __name__ == '__main__':
    main()
