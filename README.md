# Kudumbashree Management System

A web-based platform for managing Kudumbashree activities, including user registration, staff management, product tracking, and loan management.

## Features

### 👤 User Portal
- **Registration & Profile**: Secure signup with admin approval workflow.
- **Loan Management**: Apply for loans (> 1000 INR), view application status, and track weekly payments.
- **Product Booking**: Browse and book products added by production staff.
- **Attendance**: View personal attendance records.
- **Payments**: Real-time payment simulation with card validation.

### 🏭 Production Staff Portal
- **Staff Registration**: Admin-approved registration process.
- **Product Management**: Add, edit, and delete products with stock tracking and image uploads.
- **Booking Management**: View and track customer bookings for products.

### 🛡️ Admin Portal
- **User/Staff Management**: Approve, reject, block, or unblock users and staff members.
- **Attendance Tracking**: Add and view user attendance with date-based filtering.
- **Loan Administration**: Review loan applications, set durations, and monitor weekly payments.
- **Payment Monitoring**: Overview of all loan-related financial transactions.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: SQLite (Development)

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VishnuSuresh0204/Kudumbhasree.git
   cd Kudumbhasree
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   ```

3. **Install dependencies**: (Make sure to create a requirements.txt if needed)
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Design
The project features a modern, responsive design using premium aesthetics, including glassmorphism effects and custom CSS for a professional look.
