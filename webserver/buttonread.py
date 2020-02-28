import sys
import os
import sqlite3 as sql
import threading
from threading import Timer
import time
from time import gmtime, strftime
from gpiozero import Button

button = Button(2) 
flow = 5  # temp value
temp = {}
sensorids = []

cold_list = []
hot_list = []
flow_list = []


def sensor():  # find sensors
    for i in os.listdir("/sys/bus/w1/devices"):
        if i != "w1_bus_master1":
            sensorids.append(i)


def read_sensor():

    t = threading.Timer(1, read_sensor)
    t.start()

    tfile = open("/sys/bus/w1/devices/" + sensorids[0] + "/w1_slave")

    tfile2 = open("/sys/bus/w1/devices/" + sensorids[1] + "/w1_slave")

    text = tfile.read()
    tfile.close()

    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000

    text2 = tfile2.read()
    tfile2.close()

    secondline = text2.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature2 = float(temperaturedata[2:])
    temperature2 = temperature2 / 1000

    cold_temp = min(temperature, temperature2)
    hot_temp = max(temperature, temperature2)

    print(cold_temp, hot_temp, strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    with sql.connect("raspsensors.db") as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO sensordata (cold_water, hot_water, flow, currentdate, currenttime, name) VALUES (?,?,?,date('now'),time('now'),?)",
            (cold_temp, hot_temp, 1, "testname"),
        )

        con.commit()


if __name__ == "__main__":
    sensor()
    print(sensorids)
    t = Timer(10,read_sensor)

    button.wait_for_press()
    button.wait_for_release()

    time.sleep(5)

    t.start()
    
    button.wait_for_press()
    button.wait_for_release()

    t.cancel()
    read_sensor()
