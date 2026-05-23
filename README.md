# Online Quiz System

An interactive web-based quiz application built using the Django framework.  
The system allows users to register, log in, take quizzes, view scores, and download PDF certificates after completing quizzes successfully.

---

# Features

## User Authentication
- User Registration (Signup)
- User Login & Logout
- Session Management
- Secure Password Hashing using Django Authentication

## Quiz Functionality
- Multiple Choice Questions (MCQs)
- Automatic Score Calculation
- Percentage Calculation
- Quiz Result Storage

## Result Management
- View Quiz Scores
- Track User Performance
- Store Quiz Attempt History

## Certificate Generation
- PDF Certificate Download
- Dynamic User Details
- Score & Percentage Included
- Generated using ReportLab

## Admin Panel
- Add/Edit/Delete Questions
- Manage Users
- View Quiz Results
- Monitor User Performance

---

# Technology Stack

## Backend
- Python 3.14+
- Django 6.0.5

## Database
- SQLite3

## Frontend
- HTML5
- CSS3

---

# Project Structure

```bash
quizsite/
│
├── db.sqlite3
├── manage.py
│
├── quiz/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   ├── migrations/
│   └── templates/
│       ├── login.html
│       ├── signup.html
│       └── quiz/
│           ├── certificate.html
│           ├── dashboard.html
│           ├── login.html
│           ├── quiz.html
│           ├── result.html
│           ├── signup.html
│           └── teacher_dashboard.html
│
└── quizsite/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

```
# Author
Pooja Sri G
