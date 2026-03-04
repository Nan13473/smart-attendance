# Verdis Quo

Veridis Quo is a full-stack, cloud-based platform designed. It aims to automate administrative tasks such as attendance tracking, resource management (projectors/computers), and academic performance analytics. By providing dedicated interfaces for Students, Professors, and Admins, the system streamlines campus operations and improves the learning environment through data-driven insights.


This is a comprehensive `README.md` that integrates your project goals, technical implementation, and the AI-assisted development process.

---



## 🤖 AI-Assisted Development

The frontend of this project was developed using a "Human-in-the-Loop" methodology, leveraging state-of-the-art AI models:

* **Claude 3.5 Sonnet:** Utilized for building the high-fidelity UI structures, complex CSS animations (such as the bouncy role-switcher), and the responsive sidebar architectures.
* **Google Gemini:** Used for refining Vanilla JavaScript logic, optimizing API integration patterns, and ensuring cross-dashboard data consistency.

---

## 🛠️ Tech Stack

* **Backend:** Python with **Flask** framework.
* **Database:** **SQLAlchemy (ORM)** with **SQLite** for structured data storage.
* **Frontend(AI Coded):** Minimalist HTML5 and CSS3 using the **Inter** font family for a professional aesthetic.
* **Logic:** Vanilla JavaScript for real-time UI updates and dashboard navigation.

---

## 🔑 Key Features by Role

### **1. Admin Portal**

* **Student Lifecycle Management:** Interface to add new students, assign branches, and record dates of birth.
* **Database Seeding:** Automatically creates a master "Admin" account and initializes required tables on first run.

### **2. Professor Dashboard**

* **Interactive Attendance Marker(In devlopment):** A bulk-marking system that allows professors to toggle student status (Present/Absent) with live summary counts.
* **Teaching Schedule:** A dynamic weekly timetable displaying lecture times, rooms, and subject types.
* **Performance Tracking:** Overview of student grades and class-wide average scores.

### **3. Student Dashboard**

* **Attendance Analytics:** Visual progress bars for overall and subject-wise attendance percentages.
* **Monthly Calendar:** A custom-coded calendar highlighting daily attendance status (Present, Absent, or Holiday).
* **Academic Records:** Real-time tracking of CGPA trends and assignment submission statuses.


  

---

## 🚀 Implementation Progress

* **Authentication Engine:** Complete Role-Based Access Control (RBAC) that routes users to specific dashboards based on their login credentials.
* **Modular Backend:** Organized using Flask models to handle diverse datasets including `user`, `student_data`, `teacher_data`, and `admin_data`.
* **Frontend-Backend Bridge:** All dashboards are designed with placeholders and JS functions ready to consume backend API data.

---



✅ Completed Features
* Multi-Role Authentication System: Implemented a centralized login gateway that routes users to dedicated dashboards based on their role: Student (User), Professor, or Admin.

* Automated Database Initialization: The system is configured to automatically create necessary tables and seed a default "Admin" account upon the first launch.

* Secure User Onboarding: A functional Signup system for both students and faculty that includes validation logic to prevent duplicate account creation.

* Admin Management Suite: A dedicated administrative interface allowing for the manual entry of student records, including branch allocation, roll numbers, and    dates of birth.

* Dynamic Data Handling: Integration of the datetime library to handle student DOB records and age-related data.


## 📈 Roadmap

* [ ] **API Finalization:** Complete the POST routes for saving attendance data to the SQLite database.
* [ ] **Automated Alerts:** Implement a notification system for students whose attendance drops below 75%.
* [ ] **Resource Tracking:** Add modules for real-time tracking of lab equipment and projector availability.

---

## 📥 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/veridis-quo.git

```


2. **Install dependencies:**
```bash
pip install flask flask_sqlalchemy

```


3. **Run the application:**
```bash
python app.py

```

4. **Access the portal:** Click *Ctrl+Enter* or copy the address from terminal and paste it in browser.

---

* For Admin Login:-
* ID:- admin
* Pass:- Admin@1234

* *Dont forget to do signup for both teacher and professor before doing login*
* *The Admin only add data which is useful in student dashboard, login data is purely diffrent for student*

* Login data blueprint is *user.py*
* Student data blueprint is *student_data.py*
---

---

## 📋 Changelog

### v1.1 — Student ID & Attendance Tracking (2026-03-05)

#### 🆕 New Features
- **Separated `Student ID` from `Roll Number`:** These are now two distinct fields. Roll No is the physical class roll number; Student ID is the unique login credential used by the student to access their portal.
- **Admin Panel — Dual ID Entry:** The Admin form now has two separate input fields: `True Roll Number` (e.g. `54`) and `Login Student ID` (e.g. `S001`).
- **Live Attendance Dashboard for Students:** The student portal (`/user/<id>`) now fetches and displays real attendance stats from the database — Total Classes, Present, Absent, and Attendance Percentage — using server-side Jinja2 rendering.
- **Attendance linked by Student ID:** When a professor loads students for a session, their `student_id` is now stored alongside `roll_no` in the `Attendance` table, enabling the student portal to correctly look up records.

#### 🐛 Bug Fixes
- **`db.string` → `db.String`:** Fixed a fatal `AttributeError` crash during startup caused by a lowercase `s` in SQLAlchemy column definitions in `attendance.py` and `studentdata.py`.
- **Variable overwrite crash in `/user` route:** Fixed a bug where the URL `id` parameter was being overwritten by a database object, causing subsequent `count()` queries to receive an object instead of a string, crashing the route.
- **`AttributeError: NoneType`:** Fixed crash when a student logs in but has no attendance record yet — the route now fails gracefully and redirects with a message.
- **Division by Zero:** Fixed `ZeroDivisionError` in attendance percentage calculation for students with zero recorded classes.
- **Jinja `TypeError` — list vs int:** Fixed `percent_count` being stored as a list `[(val)*100]` or tuple `((val), 1)` instead of a plain number, causing Jinja2 comparisons like `{% if percent_count < 75 %}` to crash.
- **`Methods` → `methods` casing:** Fixed Flask route decorator using incorrect `Methods` (uppercase) argument which caused the route registration to silently fail.
- **Removed dead JS `fetch('/api/my_attendance')`:** The frontend was overwriting server-rendered Jinja data with a broken JavaScript API call. The JS fetch has been disabled and replaced with proper Jinja2 template variables.
- **Fixed `redirect()` incorrect kwargs:** `redirect('/', message=...)` is invalid Flask syntax; corrected to pass message via URL query string `/?message=...`.

