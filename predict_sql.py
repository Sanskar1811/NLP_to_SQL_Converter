import sqlite3
import pickle

# Load model
model = pickle.load(open("model/sql_model.pkl", "rb"))

# Get user input
query = input("Enter your question: ")
sql = model.predict([query])[0]
print(f"🧠 Predicted SQL: {sql}")

# Run SQL
conn = sqlite3.connect("data/employees.db")
cursor = conn.cursor()

try:
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("SQL Error:", e)
finally:
    conn.close()
