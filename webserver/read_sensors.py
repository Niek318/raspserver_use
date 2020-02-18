# Importeer bibliotheek voor systeemfuncties.
import sys
# Definieer een array (temp).
temp = {}
 
sensorids = ["28-011928e3ddaa"]
# loop net zo lang alles sensors af dat in het array hieboven staan.
for sensor in range(len(sensorids)):
  #tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave") #RPi 1,2 met oude kernel.
  tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave") #RPi 2,3 met nieuwe kernel.
  # Lees alle dat uit het "bestand" in een variabele.
  text = tfile.read()
  # Sluit het "bestand" nadat we het gelezen hebben.
  tfile.close()
  # We gaan nu de tekst splitsen per nieuwe regel (\n)
  # en we selecteren de 2e regel [1] (1e regel = [0])
  secondline = text.split("\n")[1]
  # Splits de regel in "woorden", er wordt gespleten op de spaties.
  # We selecteren hier het 10 "woord" [9] (tellend vanaf 0)
  temperaturedata = secondline.split(" ")[9]
  # De eerste 2 karakters zijn "t=", deze moeten we weghalen.
  # we maken meteen van de string een integer (nummer).
  temperature = float(temperaturedata[2:])
  # De temperatuurwaarde moeten we delen door 1000 voor de juiste waarde.
  temp[sensor] = temperature / 1000
  # print de gegevens naar de console.
  print "sensor", sensor, "=", temp[sensor], "graden."