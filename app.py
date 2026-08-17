from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from models import db, Task

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    status = request.args.get("status", "all")
    search = request.args.get("search", "").strip()

    query = Task.query
    if status in {"pending", "completed"}:
        query = query.filter_by(completed=(status == "completed"))
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    tasks = query.order_by(Task.deadline.asc().nullslast(), Task.created_at.desc()).all()
    total = Task.query.count()
    completed = Task.query.filter_by(completed=True).count()
    pending = total - completed

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        status=status,
        search=search,
    )

@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        deadline_raw = request.form.get("deadline", "").strip()

        if not title:
            flash("Task title is required.", "error")
            return render_template("task_form.html", task=None)

        deadline = None
        if deadline_raw:
            try:
                deadline = datetime.fromisoformat(deadline_raw)
            except ValueError:
                flash("Invalid deadline.", "error")
                return render_template("task_form.html", task=None)

        db.session.add(Task(title=title, description=description, deadline=deadline))
        db.session.commit()
        flash("Task created successfully.", "success")
        return redirect(url_for("index"))

    return render_template("task_form.html", task=None)

@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        task.title = request.form.get("title", "").strip()
        task.description = request.form.get("description", "").strip()
        deadline_raw = request.form.get("deadline", "").strip()

        if not task.title:
            flash("Task title is required.", "error")
            return render_template("task_form.html", task=task)

        if deadline_raw:
            try:
                task.deadline = datetime.fromisoformat(deadline_raw)
            except ValueError:
                flash("Invalid deadline.", "error")
                return render_template("task_form.html", task=task)
        else:
            task.deadline = None

        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for("index"))

    return render_template("task_form.html", task=task)

@app.post("/task/<int:task_id>/toggle")
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("index"))

@app.post("/task/<int:task_id>/delete")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
