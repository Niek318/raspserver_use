from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

