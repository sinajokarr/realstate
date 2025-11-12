# ✍️ Django Modular Blog & Secure Account System
***

[![Framework: Django 5.x](https://img.shields.io/badge/Framework-Django%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Architecture: CBVs & Mixins](https://img.shields.io/badge/Architecture-CBVs%20%7C%20Mixins%20%7C%20DRY-007ACC?style=for-the-badge&logo=django&logoColor=white)](https://github.com/sinajokarr)
[![Focus: User Authentication](https://img.shields.io/badge/Focus-Scalable%20User%20Model%20%26%20Auth-ff9900?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sinajokarr)
***

## 🎯 Project Overview: Modular & Secure Django Structure

In proze yek **Blog Platform** kamel ast ke ba estefade az **Django Best Practices** tarrahi shode. Hadaf-e asli, neshun dadan-e chگونگی sakht-e yek system-e modular, amn, va **highly maintainable** ba estefade az **standard Django design patterns** ast.

System az do app-e asli tashkil shode:
1.  **`account`**: Modiriyate karbaran, Custom User Model, va Authentication.
2.  **`blog`**: Modiriyate posts, CRUD operations, va content display.

---

## 🏗️ Architecture and Core Development Principles

In proze bar roye asli-tarin Mamas'e-haye Tarrahi Code mahkam ast:

### 1. **Class-Based Views (CBVs) for DRY Code**
* Estefade-ye gostarde az **Generic Views** (mesle `ListView`, `DetailView`, `CreateView`, `UpdateView`, va `DeleteView`).
* In kar be natijeh-ye yek codebase **DRY (Don't Repeat Yourself)** va **high readability** mianjamad.

### 2. **Mixin-Driven Authentication and Authorization**
* **Access Management** kamelan ba Mixin-haye built-in-e Django anjam mishavad.
* `LoginRequiredMixin`: Baraye tamin-e **authentication** karbar dar ghesmathaye mahdud.
* `UserPassesTestMixin`: Baraye **authorization** (ejazeh) va enforced kardan-e **permission rules** (masalan, ensuring the user is the post author).

### 3. **Scalable User Model**
* Estefade az **Custom User Model (`CustomUser`)** va neshun dadan-e in ba estefade az `settings.AUTH_USER_MODEL`.
* In structure, **flexibility** baraye ezafe kardan-e field-haye custom va taghyirat-e ayande ro faraham mikone.

---

## 🔒 Security & Data Flow: Authorization Diagram

Data flow-e proze, be vizhe dar ghesmathaye mahdud, ta'min konande-ye amniyat-e karbar (per-user data isolation) ast:

| Request Type | Flow / Mixins Applied | Outcome |
| :--- | :--- | :--- |
| **General** (e.g., `PostListView`) | Requests directly handled by public Views. | Public Content is Displayed. |
| **Protected (CRUD)** (e.g., `PostCreateView`) | 1. Pass through **`LoginRequiredMixin`** | If not authenticated, redirect to Login Page. |
| **Authorization** (e.g., `PostUpdateView`) | 2. Pass through **`UserPassesTestMixin`** | If `test_func()` fails (e.g., user is not the owner), return **403 Forbidden**. |
| **Success** | 3. Operation proceeds. | CRUD operation is successfully completed. |

> **Process:** Karbaran baraye anjam dadan-e operation haye **CRUD** (masalan: `PostUpdateView`) bayad avval **authenticated** bashand. Sepas, `UserPassesTestMixin` ba ejra-ye `test_func` ta'yid mikone ke aya karbar-e hal-e hazer (`self.request.user`) **ijazeh** anjam dadan-e in amal ro dare (masalan: `post.author == self.request.user`).

---

## 🛠️ Modular Structure & Next Steps

In structure ta'min konande-ye in ast ke **authentication logic (`account` app)** va **blog content logic (`blog` app)** kamelan az ham jodast, va har ghesmat asan baraye maintain va extend kardan ast.

### 🚀 Getting Started (Rahandazi)

* **Clone Repository:**
    ```bash
    git clone [Your Repository URL]
    cd [your-project-name]
    ```
* **Install Dependencies** & **Run Migrations** (Details of these steps should be in your actual `README` for completeness).

### 🙏 Call to Action

<div align="center">

***
### **I am keenly focused on building robust, clean, and secure systems using Python and Django's best practices.**

**Let's connect to discuss scalable Backend Architecture!**
***
</div>
