# Celestius Backend Recruitment Task - Event Registration API

Backend system for managing registrations for the **Backend Development Workshop**. Built with **FastAPI** and **SQLite**.

---

## 🚀 Features

- **Event Registration (`POST /register`):** Accepts student details (`name`, `email`, `department`) and saves registration with a timestamp.
- **Capacity Constraint:** Enforces a strict maximum capacity limit of 50 participants. Rejects extra registrations with `"Event is full"`.
- **Duplicate Prevention:** Rejects duplicate entries with existing email addresses with `"Duplicate registration: Email already registered"`.
- **View All Registrations (`GET /registrations`):** Retrieves the total count and list of registered participants.
- **View Single Registration (`GET /registrations/{participant_id}`):** Retrieves specific participant details by unique ID.

---

## 🛠️ Tech Stack

- **Framework:** Python / FastAPI
- **Database:** SQLite with SQLAlchemy ORM
- **Data Validation:** Pydantic

---

## 📦 Setup & Execution Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/celestius-backend-task.git](https://github.com/YOUR_USERNAME/celestius-backend-task.git)
   cd celestius-backend-task