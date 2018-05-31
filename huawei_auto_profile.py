#!/usr/bin/env python3
# coding: utf8

import datetime
import time
from concurrent.futures import ThreadPoolExecutor
from resources import Functions as f
from resources import Settings




def main():
    # Начало
    run_date = datetime.datetime.now().date()
    print('Запуск произойдет завтра после 2 часов утра...\n')
    #run_date = datetime.datetime.now().date() - datetime.timedelta(days=1)
    
    while True:
        current_date = datetime.datetime.now().date()
        if (current_date != run_date) and (datetime.datetime.now().hour >= 2):
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
            run_date = current_date
        else:
            time.sleep(60*10)
            continue


if __name__ == '__main__':
    main()
