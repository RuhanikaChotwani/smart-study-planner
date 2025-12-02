# smart-study-planner
AI Powered Smart Study Planner
# 📚 Smart Study Planner (AI-Powered)

An AI-powered study planning web application that helps students organize tasks, generate smart schedules, track progress, and understand their most productive study hours using **Machine Learning**.

This project demonstrates **full-stack development**, **AI/ML integration**, **database design**, and a **clean modern UI** — perfect for internship applications like **Google STEP**.

---

## 🚀 Features

### 🔹 Task Management
- Add tasks with name, deadline, and difficulty  
- Automatically computed priority score  
- Clean, card-based UI  

### 🔹 Smart Scheduling Algorithm
Tasks are ordered using:
- Deadline urgency  
- Difficulty weight  
- Priority formula:  
priority = difficulty × urgency
urgency = max(1, 10 - days_left)


### 🔹 Progress Tracking
- Mark tasks as completed  
- Live progress bar updates automatically  

### 🔹 Machine Learning Insight
- Uses Linear Regression on completion logs  
- Predicts **your most productive study hour**  

### 🔹 Modern UI
- Clean responsive cards  
- Easy to navigate  
- Suitable for real use  

---

## 🛠️ Tech Stack

**Frontend:**  
- HTML  
- CSS  
- JavaScript  

**Backend:**  
- Python (Flask)  

**Database:**  
- SQLite  

**Machine Learning:**  
- pandas  
- numpy  
- scikit-learn  

---

## 📂 Folder Structure



study_planner_app/
│
├── app.py # Flask backend
├── scheduler.py # Scheduling algorithm
├── ml_model.py # ML model for productive hour
├── create_db.py # Database creator
├── database.db # SQLite database
│
├── static/
│ ├── style.css # Styling
│ └── script.js # JS logic
│
└── templates/
└── index.html # Main UI


---

## How to Run Locally

### 1 Install dependencies
```bash
pip install flask pandas numpy scikit-learn

2 Create database
python create_db.py

3 Start the server
python app.py

4 Open in browser

![App Screenshot](https://github.com/user-attachments/assets/6f2819f1-7ae1-4bfe-a4c7-3d03f362d4e6)
