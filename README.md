# Smart Study Planner (AI Powered)

This is an AI-powered study planning web application that helps students organize tasks, generate smart schedules, track progress, and identify their most productive study hours using Machine Learning.

The project demonstrates full-stack development, ML integration, database design, and a clean modern interface. Suitable for resumes and internship applications such as Google STEP.

---

## UI Screenshot

![UI Screenshot](https://raw.githubusercontent.com/RuhanikaChotwani/smart-study-planner/main/Screenshot%202025-12-03%20043503.png)

---

## Features

### Task Management
- Add tasks with name, deadline, and difficulty
- Automatically generated priority score
- Simple, clean user interface

### Smart Scheduling Algorithm
Tasks are prioritized based on:
- Deadline urgency  
- Difficulty of task  

Priority formula:
priority = difficulty × urgency
urgency = max(1, 10 - days_left)

markdown
Copy code

### Progress Tracking
- Mark tasks as completed  
- Progress bar updates automatically  

### Machine Learning Insight
- Uses Linear Regression on task completion logs  
- Predicts the user's most productive study hour  

### Modern Interface
- Clean layout  
- Easy navigation  
- Practical for real use  

---

## Tech Stack

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

## Project Structure

smart-study-planner/
│
├── app.py # Flask backend
├── scheduler.py # Scheduling algorithm
├── ml_model.py # ML model for predicting productive hour
├── create_db.py # Database creation script
├── database.db # SQLite database
│
├── static/
│ ├── style.css # Stylesheet
│ └── script.js # JavaScript logic
│
└── templates/
└── index.html # Frontend UI

yaml
Copy code

---

## How to Run Locally

1. Install dependencies:
pip install flask pandas numpy scikit-learn

markdown
Copy code

2. Create the database:
python create_db.py

markdown
Copy code

3. Start the server:
python app.py

markdown
Copy code

4. Open in browser:
http://127.0.0.1:5000/

yaml
Copy code

---

## Future Improvements
- User login system  
- Edit/Delete tasks  
- Calendar view  
- Notifications and reminders  
- Dark mode  
- Deployment on Render or Vercel  

---

## Author
Ruhanika  

