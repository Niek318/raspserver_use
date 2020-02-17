import os


def sensor(): #find sensor 1
    for i in os.listdir("/sys/bus/w1/devices"):
        if i != "w1_bus_master":
            ds18b20 = i
            

    return ds18b20

def read(ds18b20): #read data from sensor
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open.location
    text = tfile.read()
    tfile.close()

    secondline = text.split("\n")[1]
    tempdata = secondline.split(" ")[9]
    temp = float(tempdata[2:])
    celcius = temp / 1000
    return celcius

def loop(ds18b20): #change to either save to file or directly to database
    while True:
        if read(ds18b20) != None:
            print "Current temp : %0.3f C" % read(ds18b20)


def kill():
    quit()

if __name__ == "__main__":
    try:
        serialNum = sensor()
        loop(serialNum)
    except: KeyboardInterrupt:
        kill()