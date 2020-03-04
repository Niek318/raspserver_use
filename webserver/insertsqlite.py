import sqlite3
from time import gmtime, strftime

conn = sqlite3.connect("showerdata.db")

c = conn.cursor()
time = strftime("%m-%d", gmtime())
print(time)
c.execute(
    "INSERT INTO showerdata(cold_water, hot_water, flow, shower_time, date_time, money_saved) VALUES (?,?,?,?,?,?)",
    (6, 26, 12, 55, time, 1),
)

conn.commit()

conn.close()
