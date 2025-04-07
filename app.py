from flask import Flask, render_template, request
import sqlite3
import pickle

app = Flask(__name__)
model = pickle.load(open("model/sql_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    sql = ""
    results = []
    
    if request.method == "POST":
        query = request.form["query"]
        sql = model.predict([query])[0]

        try:
            conn = sqlite3.connect("data/employees.db")
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.close()
        except Exception as e:
            results = [("Error", str(e))]

    return render_template("index.html", query=query, sql=sql, results=results)

if __name__ == "__main__":
    app.run(debug=False)
