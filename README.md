# 🚀 Gas Utility Service API

### ✅ Developed for HCL Internal Operations Case Study
A real-time gas utility management system to handle service requests, track request status, and provide tools for customer support.

---

## 📚 Project Overview

This project simulates a **Gas Utility Service Platform** that allows customers to:
- Submit service requests (e.g., gas connection issues, billing inquiries).
- Track the status of requests.
- Admins and support staff can manage and monitor service requests efficiently.

---

## 📚 Features
✅ **User Authentication & Role-Based Access (RBAC)**
- Admin, Customer, and Support Roles.
- JWT Token-based Authentication.
- Auto-refresh of tokens in Postman.

✅ **Service Request Management**
- Create, View, Update, and Delete Service Requests.
- Role-Based Restrictions (Customers can only manage their own requests).
- Admin and Support can view, update, and delete any request.

✅ **Request Tracking & Notifications**
- Track the status of service requests.
- Email notifications on status updates (Planned for future sprints).

✅ **Admin Support Tools**
- Manage Service Types and Request Statuses.
- CRUD Operations for Master Data.

---

## 📚 Technology Stack

| Technology         | Description                  |
|--------------------|------------------------------|
| Django             | Web Framework (Backend)      |
| Django REST Framework | REST API Development    |
| PostgreSQL         | Database Management System   |
| JWT Authentication | Secure Token-based Auth      |
| Redis              | Caching and Performance      |
| Postman            | API Testing                  |
| Docker             | Containerization (Planned)   |
| AWS                | Deployment (Future Scope)    |

---

## 📚 Folder Structure
