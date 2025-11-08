# 🗓️ Django To-Do App

A simple and responsive **To-Do List web app** built using **Django**, **Bootstrap 5**, and **Font Awesome**.  
This project allows users to add, edit, mark as complete, and delete daily tasks — all from a clean, modern interface.

---

## 🚀 Features

✅ Add new tasks  
✏️ Edit existing tasks  
✅ Mark tasks as completed  
❌ Delete tasks  
↩️ Unmark completed tasks  
📱 Fully responsive design  

---

## 🛠️ Technologies Used

- **Python 3**
- **Django 5**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **Font Awesome Icons**

---
## 📂 Project Structure
Django-Projects/
│
├── todo/ # Django project folder
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── tasks/ # Django app folder
│ ├── templates/ # HTML files
│ │ ├── index.html
│ │ └── edit.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── .gitignore


---

## ⚙️ Installation & Setup

Follow these steps to run the project locally 👇

### 1️⃣ Clone this repository
```bash
git clone https://github.com/yourusername/Django-Projects.git
cd Django-Projects

2️⃣ Create a virtual environment
python -m venv env

3️⃣ Activate the environment
On Windows:
env\Scripts\activate

On Mac/Linux:
source env/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run database migrations
python manage.py migrate

6️⃣ Run the server
python manage.py runserver


Then open your browser and go to 👉 http://127.0.0.1:8000/

🧠 How It Works

Tasks are stored in a SQLite3 database by default.

Each task has:

A name (text)

A status (complete / incomplete)

A timestamp (when last updated)

Django’s ORM handles all database operations.

💡 Future Improvements

Add user authentication (login/register)

Enable due dates for tasks

Add category filters (Work, Personal, etc.)

Add dark mode UI

🧑‍💻 Author

Swathi Sivakumar
💼 GitHub: @Swathisivakumar157


⭐ If you found this project useful, give it a star on GitHub!

---




