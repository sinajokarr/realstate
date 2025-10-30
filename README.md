🏗️ Project Architecture and Overview
This project adheres to standard Django design patterns and best coding practices, providing a modular and secure structure. The system's architecture is based on two primary applications: account and blog.

1. Architecture and Core Development Principles
Class-Based Views (CBV): Extensive use of Generic Views (such as ListView, DetailView, CreateView, UpdateView, and DeleteView) to ensure a DRY (Don't Repeat Yourself) codebase and maintain high readability.

Mixin-Driven Authentication: Access management is handled by native Django Mixins, specifically LoginRequiredMixin (to ensure user authentication) and UserPassesTestMixin (to enforce specific permission rules, like post ownership).

Scalable User Model: By utilizing settings.AUTH_USER_MODEL, the project supports a Custom User Model (CustomUser) for future flexibility and additional custom fields.

2. Data Flow and Authorization Diagram
The main request flow in the project is as follows:

General Requests: Requests related to viewing content (e.g., PostListView and PostDetailView) are handled directly by public Views.

Protected Requests (CRUD):

Requests for creating, editing, or deleting posts (e.g., PostCreateView, PostUpdateView, PostDeleteView) first pass through the LoginRequiredMixin filter. If the user is not logged in, they are redirected to the login page.

Upon successful login, the request proceeds to UserPassesTestMixin. This Mixin executes the test_func method to verify that the current user (self.request.user) is authorized to perform the operation (e.g., confirming that post.author == self.request.user).

If approved, the operation proceeds; otherwise, access is Forbidden (403).

3. Modular Structure
This structure ensures that the authentication logic and the blog content logic are completely decoupled, making each section easy to maintain and extend.
