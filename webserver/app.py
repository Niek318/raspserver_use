from flask import Flask, render_template, request, redirect
import sqlite3 as sql
import pandas as pd

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return redirect("/home")


@app.route("/enternew")
def new_student():
    return render_template("enternew.html")


@app.route("/addrec", methods=["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            cold = request.form["cold"]
            hot = request.form["hot"]
            flow = request.form["flow"]
            name = request.form["name"]

            with sql.connect("raspsensors.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO sensordata (cold_water, hot_water, flow, currentdate, currenttime, name) VALUES (?,?,?,date('now'),time('now'),?)",
                    (cold, hot, flow, name),
                )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route("/list")
def list():
    con = sql.connect("showerdata.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from showerdata")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

@app.route("/home")
def saved():
    conn = sql.connect(
    "showerdata.db", isolation_level=None, detect_types=sql.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT id, hot_water, flow, date_time, cold_water, money_saved FROM showerdata", conn)
    db_df.to_csv("database.csv", index=False)

    csv = pd.read_csv("database.csv", header=0, index_col=0, parse_dates=True, squeeze=True)
    saved = csv['money_saved'].sum()
    return render_template("home.html", totalmoneysaved=saved, totalenergysaved = saved*(35170000/0.82))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False) #host='0.0.0.0',

