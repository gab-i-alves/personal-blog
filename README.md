# Personal Blog Project

A personal blog application designed to write and publish articles on various topics. Inspired by the project ideas from [roadmap.sh](https://roadmap.sh) and built using Django, this project serves as a practice platform for learning backend development, templating, and basic authentication.

---

## Project Features

### Guest Section (Accessible to Everyone)
1. **Home Page**: Displays a list of published articles.
2. **Article Page**: Displays the content of a specific article along with its publication date.

### Admin Section (Accessible to Admin Only)
1. **Dashboard**: 
   - List all articles.
   - Options to add, edit, or delete articles.
2. **Add Article Page**: A form to create a new article.
3. **Edit Article Page**: A form to edit an existing article.

---

## Project Setup

### Prerequisites
- Python 3.8+
- Django 4.x
- A text editor or IDE
- Git

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gab-i-alves/personal-blog.git
   cd personal-blog
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Start the Django Project**:
   ```bash
   django-admin startproject personal_blog .
   python3 manage.py startapp blog
   ```

---

## To-Do List

### 1. Models
- [X] Create an `Article` model with fields:
  - `title` (CharField)
  - `content` (TextField)
  - `date_published` (DateTimeField)
- [X] Run migrations to apply the model.

### 2. Views
- [ ] Create views for the **Guest Section**:
  - [ ] `Home Page`: List all articles.
  - [ ] `Article Page`: Display a single article.
- [ ] Create views for the **Admin Section**:
  - [ ] `Dashboard`: Manage articles (add, edit, delete).
  - [ ] `Add Article Page`: Form to create an article.
  - [ ] `Edit Article Page`: Form to edit an article.

### 3. URLs
- [ ] Define URL patterns for the **Guest Section**:
  - `/` → Home Page
  - `/article/<id>/` → Article Page
- [ ] Define URL patterns for the **Admin Section**:
  - `/admin/dashboard/` → Dashboard
  - `/admin/add-article/` → Add Article Page
  - `/admin/edit-article/<id>/` → Edit Article Page

### 4. Templates
- [ ] Create templates for:
  - [ ] Home Page (`home.html`)
  - [ ] Article Page (`article.html`)
  - [ ] Dashboard (`dashboard.html`)
  - [ ] Add/Edit Article Page (`form.html`)

### 5. Authentication
- [ ] Implement Django's authentication system.
  - [ ] Protect admin pages with `@login_required`.
  - [ ] Add a login form for the admin.

### 6. Styling
- [ ] Add basic CSS styling for pages.
- [ ] Ensure responsiveness for mobile and desktop views.

### 7. Deployment
- [ ] Test the application locally.
- [ ] Deploy the project to a platform like Heroku, Render, or PythonAnywhere.

---

## Optional Features (Stretch Goals)
- [ ] Add article categories/tags.
- [ ] Implement search functionality for articles.
- [ ] Enable comments on articles.
- [ ] Add pagination for the Home Page.
- [ ] Allow file uploads for images in articles.
- [ ] Integrate a WYSIWYG editor for rich text editing.

---

## Running the Application
1. Start the development server:
   ```bash
   python3 manage.py runserver
   ```
2. Open the app in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.