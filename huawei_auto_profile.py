#!/usr/bin/env python3
# coding: utf8

from concurrent.futures import ThreadPoolExecutor
from resources import Functions as f
from resources import Settings




def main():
    print('Получение данных из SQL-базы...')
    sql_data = f.get_sql_data()
    print('\nДанные для работы получены. Запуск обработки DSLAM...\n')
    
    arguments = [(host, sql_data) for host in Settings.hosts]
    
    with ThreadPoolExecutor(max_workers=Settings.threads) as executor:
        executor.map(f.run, arguments)



if __name__ == '__main__':
    main()