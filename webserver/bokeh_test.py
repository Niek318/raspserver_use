from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
import pandas as pd
import sqlite3
import bokeh.sampledata
from matplotlib import pyplot


# # prepare some data
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]

# # output to static HTML file
# output_file("lines.html")

# # create a new plot with a title and axis labels
# p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")

# # add a line renderer with legend and line thickness
# p.line(x, y, legend="Temp.", line_width=2)

# # show the results
# show(p)


conn = sqlite3.connect(
    "showerdata.db", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES
)
db_df = pd.read_sql_query(
    "SELECT id, hot_water, flow, date_time, cold_water, money_saved FROM showerdata", conn
)
db_df.to_csv("database.csv", index=False)


csv = pd.read_csv("database.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
csv.plot(x="date_time")
pyplot.show()


# csv["date_time"] = pd.to_datetime(csv["date_time"])
#
# p = figure(x_axis_type="datetime")
# p.line(csv["date_time"], csv["flow"], color="navy", alpha=0.5)
# p.line(csv["date_time"], csv["cold_water"], color="navy", alpha=0.5)
#
# show(p)


print(csv)
output_file("lines.html")

