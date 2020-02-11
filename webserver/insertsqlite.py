import sqlite3
conn = sqlite3.connect('raspsensors.db')

c = conn.cursor()

c.execute("INSERT INTO sensordata(cold_water, hot_water, flow, currentdate, currenttime,name) VALUES (2,22,4,date('now'),time('now'),'niek')")

conn.commit()

conn.close()
