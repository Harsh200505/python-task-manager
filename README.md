📝 Python Task Manager

A simple and fully functional Task Management Web Application built with Python and Flask.

This project allows users to create, edit, complete, search, filter, and delete tasks through a clean web interface. Task data is stored persistently using SQLite and managed through SQLAlchemy.

---

🚀 Features

- ✅ Create new tasks
- ✏️ Edit existing tasks
- 🗑️ Delete tasks
- ✔️ Mark tasks as completed
- 🔄 Mark completed tasks as pending
- 📅 Add task deadlines
- 📝 Add task descriptions
- 🔍 Search tasks
- 📋 Filter tasks by status
- 📊 View total, pending, and completed task counts
- 💾 Persistent SQLite database
- 📱 Responsive interface

---

🛠️ Tech Stack

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- Jinja2

---

📂 Project Structure

python-task-manager/
│
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignored files
│
├── templates/
│   ├── base.html          # Base HTML layout
│   ├── index.html         # Task dashboard
│   └── task_form.html     # Add/Edit task form
│
└── static/
    └── style.css          # Application styling

---

⚙️ How It Works

The application follows a simple Flask-based architecture:

User
  ↓
Web Browser
  ↓
Flask Routes
  ↓
Application Logic
  ↓
SQLAlchemy ORM
  ↓
SQLite Database
  ↓
Task Data
  ↓
Jinja2 Templates
  ↓
Web Browser

---

🗄️ Database

The application uses SQLite for storing task information.

Each task contains:

Field| Description
"id"| Unique task ID
"title"| Task title
"description"| Task description
"deadline"| Optional deadline
"completed"| Task completion status
"created_at"| Task creation date/time

The database is automatically created when the Flask application starts.

---

🔗 Application Routes

Route| Method| Description
"/"| GET| Displays the task dashboard
"/task/add"| GET, POST| Creates a new task
"/task/<id>/edit"| GET, POST| Updates a task
"/task/<id>/toggle"| POST| Changes task completion status
"/task/<id>/delete"| POST| Deletes a task

---

💻 Installation & Setup

1. Clone the repository

git clone https://github.com/Harsh200505/python-task-manager.git

2. Open the project

cd python-task-manager

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows PowerShell

venv\Scripts\activate

Windows Command Prompt

venv\Scripts\activate

5. Install dependencies

python -m pip install -r requirements.txt

6. Run the application

python app.py

7. Open in your browser

http://127.0.0.1:5000

---

📸 Screenshots

Add a "screenshots" folder to the project:

screenshots/
├── dashboard.png
├── add-task.png
└── completed-task.png

Then add your screenshots below.

🏠 Dashboard

"Task Manager Dashboard" (screenshots/dashboard.png)

➕ Add Task

"Add Task" (screenshots/add-task.png)

✅ Completed Task

"Completed Task" (screenshots/completed-task.png)

---

🎯 Main Functionality

Create Task

Users can create a task by entering:

- Task title
- Description
- Deadline

Manage Tasks

Users can:

- Edit tasks
- Delete tasks
- Complete tasks
- Reopen completed tasks

Search & Filter

Tasks can be searched by title and filtered according to their completion status.

Dashboard

The dashboard displays:

Total Tasks
Pending Tasks
Completed Tasks

---

🔐 Security

This project is currently designed as a learning and portfolio project.

Before deploying it to production, additional security features should be added, such as:

- CSRF protection
- User authentication
- Environment variables for secrets
- Production server configuration
- Database migration system
- Input validation

---

🔮 Future Improvements

Future versions could include:

- 👤 User registration and login
- 🔐 Authentication
- ⭐ Task priorities
- 🏷️ Task categories
- 🔔 Deadline notifications
- 📱 Progressive Web App support
- 🌙 Dark mode
- 🔌 REST API
- ☁️ Cloud database
- 🚀 Online deployment

---

📚 Learning Outcomes

Through this project, I practiced:

- Python programming
- Flask web development
- CRUD operations
- SQLite database management
- SQLAlchemy ORM
- HTML forms
- Jinja2 templating
- CSS styling
- Form validation
- Search and filtering
- Virtual environments
- Git & GitHub

---

👨‍💻 Author

Harsh Wardhan

Computer Science Engineering Student

Built with ❤️ using Python and Flask.

---

⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

📄 License

This project is available for educational and personal use.
