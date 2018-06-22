# coding: utf8

# Учетные данные DSLAM
login_5600 = ''
password_5600 = ''
login_5616 = ''
password_5616 = ''

#Количество потоков выполнения
threads = 10

#Запас скорости
threshold_delta = 8
before_delta = 1
after_delta = 3

#Скорость ('AVG' - средняя, 'MIN' - минимальная)
speed = 'MIN'

#Интервал запуска (часов)
run_interval = 6

#Список DSLAM
hosts = (('ip', 'model'),)
         
# Mysql
db_host = ''
db_user = ''
db_password = ''
db_name = ''
