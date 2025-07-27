# Django Blog with REST API

A full-featured blog application built with **Django** and enhanced with a **REST API** using **Django REST Framework (DRF)**.  
The project includes user authentication, CRUD operations, permissions, API documentation, and is ready for further expansion.

---

## 📝 Features

- **User Authentication**
  - Sign up, login, logout
  - Password change and reset
- **Blog Functionality**
  - Create, read, update, delete (CRUD) posts
  - Categories for organizing posts
  - Pagination
  - Comments on posts
- **REST API**
  - Full API endpoints for posts and users
  - Token-based authentication
  - Permissions: only authors can edit/delete their own posts
  - Browsable API interface
- **Documentation**
  - Interactive API documentation via Swagger UI and ReDoc
- **Frontend**
  - Responsive design using Bootstrap
  - Clean Blog template from Start Bootstrap

---

## 🛠️ Technologies Used

- Python 3.x
- Django 5.2
- Django REST Framework (DRF)
- drf-spectacular — for OpenAPI schema and documentation
- dj-rest-auth & django-allauth — for user registration and authentication
- SQLite (default, easily switchable to PostgreSQL)
- Bootstrap 5 + Crispy Forms

---

## 🧪 Testing

- Unit tests for models and views
- API tests for endpoints and permissions

---

## 🚀 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/pydaemon/django-blog.git
   cd django-blog
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**

   ```bash
   python manage.py runserver
   ```

7. **Open in browser**

   Visit [http://localhost:8000](http://localhost:8000)

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/api/v1/` | GET, POST | List all posts or create a new one |
| `/api/v1/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update or delete a post |
| `/api/v1/users/` | GET | List all users (Admin only) |
| `/api/v1/dj-rest-auth/registration/` | POST | Register a new user |
| `/api/v1/dj-rest-auth/login/` | POST | Login and get token |
| `/api/v1/dj-rest-auth/logout/` | POST | Logout and invalidate token |

> Authorization required for GET, POST, PUT, PATCH, DELETE methods

---

## 🔒 Authentication

- Uses **Token Authentication** via `dj-rest-auth`
- Only authenticated users can create/edit posts
- Only the author of a post can edit/delete it
- Admin users have full access

---

## 📄 API Documentation

You can view and test the API endpoints interactively:

- **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
- **ReDoc**: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

---

## 📁 Project Structure

```
django-blog/
├── blog/                  # Blog models, views
├── accounts/              # Custom user model and auth
├── apis/                  # REST API logic
├── django_project/        # Settings, URLs, WSGI
├── static/                # Static assets (Bootstrap, CSS, JS)
├── templates/             # HTML templates
├── manage.py
├── .gitignore
├── requirements.txt
└── README.md

```

---

## 🧪 Running Tests

To run all tests:

```bash
python manage.py test
```

---

## 🚀 Deployment Notes

This project uses standard Django deployment practices:
- Use WSGI or ASGI for production (ASGI recommended if planning async features)
- Set `DEBUG = False` in production settings
- Use environment variables for secrets (e.g., `DJANGO_SECRET_KEY`)
- Consider PostgreSQL or MySQL for production databases
- Serve static files via Whitenoise or Nginx

For more info, see [Django deployment docs](https://docs.djangoproject.com/en/5.2/howto/deployment/)

---

## 📸 Screenshots (Coming soon)



---

## 🧾 License

MIT License — feel free to use this code as a base for your own projects.
```