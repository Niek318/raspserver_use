import sys
import os
import sqlite3 as sql
import threading
from time import gmtime, strftime


temp = {}
sensorids = []


def sensor():  # find sensors
    for i in os.listdir("/sys/bus/w1/devices"):
        if i != "w1_bus_master1":
            sensorids.append(i)


sensor()
print(sensorids)


def read_sensor():

    threading.Timer(5.0, read_sensor).start()

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


read_sensor()

# with sql.connect("raspsensors.db") as con:
# cur = con.cursor()
# cur.execute(
#     "INSERT INTO sensordata (cold_water, hot_water, flow, currentdate, currenttime, name) VALUES (?,?,?,date('now'),time('now'),?)",
#         (temp[sensor], temp[sensor], 1, "testname"),
#     )

# con.commit()

