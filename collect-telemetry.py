import time
from random import random
from random import seed

import pymysql.cursors

seed(1)
# These methods should be used to read your sensor values.


def read_sensor_1():
    return random()


def read_sensor_2():
    return random()


def read_sensor_3():
    return random()


def read_sensor_4():
    return random()


print("Connecting to the database")
connection = pymysql.connect(host='localhost',
                             user='telemetry',
                             password='xldfbgsdbfbladfvasd',
                             database='telemetry',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)

with connection:
    with connection.cursor() as cursor:
        sql = "insert into telemetry (timestamp, sensor1, sensor2, sensor3, sensor4) values (now(), %s, %s, %s, %s);"
        print("Inserting data")
        i = 0
        while True:
            if i % 10 == 0 and i > 0:
                print("Wrote {} values".format(i))

            # Create a new record

            sensor1 = read_sensor_1()
            sensor2 = read_sensor_2()
            sensor3 = read_sensor_3()
            sensor4 = read_sensor_4()

            cursor.execute(sql, (sensor1, sensor2, sensor3, sensor4))

            # Sleep 200ms. Meaning that we will only execute this loop every 200 ms
            time.sleep(.200)
            i += 1
