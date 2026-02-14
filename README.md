# Tourney - Turf Booking System

A streamlined Django-based web application for managing turf bookings. Owners can register their turfs and packages, while users can search for turfs and book play sessions.

## 🚀 Features

- **User Authentication**: Secure login and registration for Admins, Users, and Turf Owners.
- **Turf Management**: Dedicated dashboard for Turf Owners to manage their properties and session packages.
- **Booking System**: Users can search for turfs by district and location, view available packages, and book slots.
- **Admin Dashboard**: Centralized control for managing districts, locations, and approving/rejecting user and turf registrations.
- **Notifications & Feedback**: System for users to provide feedback and for owners to handle bookings.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (Small, portable, and efficient)
- **Frontend**: HTML5, CSS3 (SB Admin 2 template), JavaScript (jQuery, Bootstrap)
- **Environment**: Python Virtual Environment (`venv`)

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alameenShameer/Tourney.git
   cd Tourney/turffinal
   ```

2. **Set up the Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django requests
   ```

4. **Initialize the Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Seed Test Data** (Optional but recommended):
   ```bash
   python seed_data.py
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver 8001
   ```
   Access the app at `http://127.0.0.1:8001/`.

## 👥 Demo Accounts

| Role | Username | Password |
| :--- | :--- | :--- |
| **Admin** | `admin` | `admin123` |
| **User** | `user` | `user123` |
| **Turf Owner** | `turf` | `turf123` |

## 📁 Project Structure

- `tapp/`: Main application directory containing models, views, and templates.
- `turf/`: Project configuration settings and URL rooting.
- `media/`: Directory for uploaded package images and files.
- `templates/`: HTML templates organized by functional areas.

## 🧹 Refactoring Notes

This project has been recently refactored to:
- Remove legacy "Shop" and "Club" features.
- Switch from MySQL to SQLite for easier portability.
- Modularize view logic for better maintainability.
- Clean up unused templates and routes.
