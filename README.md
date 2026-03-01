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

4. **Access the portal:** Open your browser and navigate to `http://0.0.0.0:3000`.

---

For Admin Login:-
ID:- admin
Pass:- Admin@1234

* *Dont forget to do signup for both teacher and professor before doing login*
* *The Admin only add data which is useful in student dashboard, login data is purely diffrent for student*

* Login data blueprint is *user.py*
* Student data blueprint is *student_data.py*
---

