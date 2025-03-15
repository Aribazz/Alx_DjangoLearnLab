# 📖 Django REST API - Book & Author Management

## 🚀 Overview
This API allows users to manage books and authors. It supports CRUD operations and includes authentication and permission controls.

---

## 📌 Features
- **Retrieve all books** (`GET /api/books/`)
- **Retrieve a single book** (`GET /api/books/<id>/`)
- **Create a book** (`POST /api/books/`) 🔒 (Requires authentication)
- **Update a book** (`PUT /api/books/<id>/`) 🔒 (Requires authentication)
- **Delete a book** (`DELETE /api/books/<id>/`) 🔒 (Requires authentication)
- **Filter books by author name & publication year**

---

## 📂 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/advanced_api_project.git
cd advanced_api_project
