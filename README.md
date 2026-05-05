# PBAC — Policy-Based Access Control & Expense Management

A Django application implementing policy-based access control for expense management workflows. Features custom user authentication, role-based permissions, approval workflows, and database-level indexing for query performance.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Django 5.x |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth | Custom User Model (AbstractBaseUser) |
| Permissions | Django's built-in permission framework + custom policies |
| Templates | Django Template Language |

## Features

- **Custom User Model** — Email-based authentication replacing Django's default username system
- **Role-Based Access** — Staff, Customer, and Admin roles with Django's `PermissionsMixin`
- **Expense Approval Workflow** — Status transitions: Pending → Approved/Rejected → Reimbursed
- **Custom Permissions** — `can_approve_expense` permission for fine-grained authorization
- **Database Indexing** — Compound indexes on status/date and staff/status for query optimization
- **Password Recovery** — Full password reset flow with email confirmation

## Data Models

```
CustomUser ──┐
             ├── Staff ──── Expenses ──── Customer
             │              (status workflow)
             └── (PermissionsMixin for RBAC)
```

- **CustomUser** — Email-based auth with `CustomUserManager`
- **Staff** — Employee profiles linked to users (employee_id, position, hire_date)
- **Customer** — External customer records
- **Expenses** — Financial records with 4-state status workflow and audit timestamps

## Quick Start

```bash
# Clone
git clone https://github.com/fardanahmed/pbac.git
cd pbac

# Virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Project Structure

```
pbac/
├── accounts/
│   ├── models.py        # CustomUser, Staff, Customer, Expenses
│   ├── backends.py      # Custom authentication backend
│   ├── views.py         # Auth and expense views
│   └── migrations/      # Database migrations
├── config/
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI entry point
├── templates/           # HTML templates (login, expense views)
├── manage.py
└── requirements.txt
```

## License

MIT
