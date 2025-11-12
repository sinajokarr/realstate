# ✍️ Django Modular Blog & Secure Account System
***

[![Framework: Django 5.x](https://img.shields.io/badge/Framework-Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Architecture: CBVs & Mixins](https://img.shields.io/badge/Architecture-CBVs%20%7C%20Mixins%20%7C%20DRY-007ACC?style=for-the-badge&logo=django&logoColor=white)](https://github.com/sinajokarr)
[![Focus: User Authentication](https://img.shields.io/badge/Focus-Scalable%20User%20Model%20%26%20Auth-ff9900?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sinajokarr)
***

## 🎯 Project Overview: Modular & Secure Django Structure

This project delivers a complete **Blog Platform** built using **Django 5 best practices**. The primary goal is to showcase the creation of a modular, secure, and **highly maintainable system** using standard Django design patterns.

The system's logic is cleanly separated into two primary applications:
1.  **`account`**: Manages users, the Custom User Model, and all Authentication logic.
2.  **`blog`**: Handles post content, CRUD operations, and content display.

---

## 🏗️ Core Architecture and Development Principles

The project adheres to principles of **clean architecture** and **code efficiency**:

### 1. **Class-Based Views (CBVs) for DRY Code**
* **Extensive use** of Django's Generic Views (e.g., `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`).
* This approach ensures a **DRY (Don't Repeat Yourself)** codebase and maintains **high readability**, making it scalable for future feature additions.

### 2. **Mixin-Driven Authentication and Authorization**
* Access management is entirely handled by native Django Mixins for clear security rules.
* **`LoginRequiredMixin`**: Ensures user **authentication** is mandatory for protected routes.
* **`UserPassesTestMixin`**: Enforces specific **authorization** rules, primarily to confirm resource ownership (e.g., only the post author can edit the post).

### 3. **Scalable Custom User Model**
* The system uses a **Custom User Model (`CustomUser`)** referenced via `settings.AUTH_USER_MODEL`.
* This provides necessary **flexibility** for adding custom fields and integrating with external authentication/authorization services in the future.

---

## 🔒 Security & Data Flow: Authorization Process

The data flow for protected requests clearly illustrates the **multi-layer security checks** implemented by the Mixins:

| Request Type | Mixins Applied | Function/Check | Outcome |
| :--- | :--- | :--- | :--- |
| **Protected (CRUD)** | 1. `LoginRequiredMixin` | Checks if the user is **Authenticated**. | If unauthorized, redirects to Login page. |
| **Authorization** (e.g., `PostUpdateView`) | 2. `UserPassesTestMixin` | Executes `test_func()` to verify **Ownership/Permission**. | If check fails (e.g., not the author), returns **403 Forbidden**. |
| **Success** | N/A | Operation proceeds. | CRUD action is safely performed. |

---

## 🚀 Getting Started (Setup Guide)

To run this project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL]
    cd [your-project-name]
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate # For macOS/Linux
    # .\venv\Scripts\activate # For Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations and Create Superuser:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser # For accessing the Django Admin
    ```

5.  **Start the Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at **`http://127.0.0.1:8000/`**.

---

## 🙏 Call to Action

<div align="center">

***
### **This project confirms my commitment to building robust, clean, and secure systems using Python and Django's best practices.**

**Let's connect to discuss how to optimize your Backend Architecture for security and scalability!**
***
</div>
