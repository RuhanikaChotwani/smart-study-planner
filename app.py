from flask import Flask, render_template, request, jsonify
import sqlite3
from scheduler import generate_schedule
from ml_model import predict_best_hour

app = Flask(__name__)

# ------------------ DATABASE ------------------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ------------------ HOME ------------------
@app.route("/")
def index():
    return render_template("index.html")

# ------------------ ADD TASK ------------------
@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.json
    task = data["task"]
    deadline = data["deadline"]
    difficulty = data["difficulty"]

    conn = get_db()
    conn.execute("INSERT INTO tasks (task, deadline, difficulty) VALUES (?, ?, ?)",
                 (task, deadline, difficulty))
    conn.commit()
    return jsonify({"message": "Task added"})

# ------------------ COMPLETE TASK ------------------
@app.route("/complete_task", methods=["POST"])
def complete_task():
    data = request.json
    task_id = data["task_id"]

    conn = get_db()
    conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.execute(
        "INSERT INTO logs (task_id, completion_hour) VALUES (?, strftime('%H','now'))",
        (task_id,)
    )
    conn.commit()

    return jsonify({"message": "Task completion logged"})

# ------------------ GET SCHEDULE + PROGRESS ------------------
@app.route("/get_schedule", methods=["GET"])
def get_schedule():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()

    schedule = generate_schedule(tasks)

    # progress
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"] == 1])
    progress = int((completed / total) * 100) if total > 0 else 0

    return jsonify({
        "tasks": schedule,
        "progress": progress
    })

# ------------------ ML PREDICTION ------------------
@app.route("/best_hour", methods=["GET"])
def best_hour():
    hour = predict_best_hour()
    return jsonify({"best_hour": hour})

if __name__ == "__main__":
    app.run(debug=True)
