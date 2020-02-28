import sys
import os
import sqlite3 as sql
import threading
from threading import Timer
import time
from time import gmtime, strftime
import math
from gpiozero import Button




button = Button(17) 
flow = 5.0  # temp value
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

    cold_list.append(cold_temp)
    hot_list.append(hot_temp)
    flow_list.append(flow)

  
    print(cold_temp, hot_temp, strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    # with sql.connect("raspsensors.db") as con:
    #     cur = con.cursor()
    #     cur.execute(
    #         "INSERT INTO sensordata (cold_water, hot_water, flow, currentdate, currenttime, name) VALUES (?,?,?,date('now'),time('now'),?)",
    #         (cold_temp, hot_temp, 1, "testname"),
    #     )

    #     con.commit()


def Average(lst): 
    print(float(sum(lst) / len(lst)))
    return float(sum(lst) / len(lst)) 

if __name__ == "__main__":
    sensor()
    print(sensorids)
    showertime = 0
    while True:
        start = time.time()
        button.wait_for_press()
        button.wait_for_release()


        while not button.is_pressed:
            read_sensor()
            time.sleep(1)
            type(hot_list[0])
  

        
        button.wait_for_press()
        button.wait_for_release()
        end = time.time()
        elapsed = end - start
        print("stopped measuring, showertime = %d minutes and %d  seconds" % (math.floor(elapsed/60), elapsed%60))
        
        print("average values of cold temp: %d, hot temp: %d and flow: %d."% (Average(cold_list), Average(hot_list), Average(flow_list)))
        time.sleep(4)

        
