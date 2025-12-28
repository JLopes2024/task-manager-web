from flask import Flask, render_template, request, redirect, url_for
from database import init_db
from services import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
)

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        add_task(request.form["title"])
        return redirect(url_for("index"))

    tasks = list_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>")
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
