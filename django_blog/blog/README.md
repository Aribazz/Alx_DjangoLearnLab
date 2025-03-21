# 📝 Blog Post Application (Django)
This Django-based blog application allows users to create, read, update, and delete blog posts. 

## 🚀 Features
- ✅ **View all posts** – Public access to browse blog posts.
- ✅ **View individual posts** – Public access to read full blog content.
- ✅ **Create posts** – Only logged-in users can create new posts.
- ✅ **Edit posts** – Only the **author** of a post can edit it.
- ✅ **Delete posts** – Only the **author** of a post can delete it.

## 🔒 Permissions & Access Control
| Feature       | Who Can Access? |
|--------------|----------------|
| View Posts   | Everyone (Public) |
| Create Post  | Authenticated Users |
| Edit Post    | Only the Post Author |
| Delete Post  | Only the Post Author |

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/blog-app.git
cd blog-app
