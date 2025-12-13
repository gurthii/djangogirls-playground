# My take on the "Django Girls Blog" tutorial project
A simple, functional web blog built using Python and Django. This project is an implementation of the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/).

## Intro
This application allows users to view blog posts and includes an administration interface for content management. It was built to learn the fundamentals of web development with Django, including models, views, templates, and deployment. You can view it live on my [PythonAnywhere Web App](https://mandra.pythonanywhere.com/)

## Features
* **Blog Posts**: View a list of posts and read full articles.
* **Content Management**: Create, edit, and publish posts via the Django Admin panel or frontend forms.
* **Responsive Design**: Styled with CSS to look good on different devices.
* **Database**: Uses SQLite (default) for storing blog data.

##  Technologies Used
* **Python** (Backend logic)
* **Django** (Web framework)
* **HTML/CSS** (Frontend templates and styling)
* **Bootstrap** (For layout and design components)

## Getting Started
### Prerequisites
* Python 3.x installed
### Installation
1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/my-first-blog.git](https://github.com/your-username/my-first-blog.git)
cd my-first-blog
```
2. **Create and activate a virtual environment:**      
```bash
# Windows
python -m venv myvenv
myvenv\Scripts\activate

# macOS/Linux
python3 -m venv myvenv
source myvenv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Apply database migrations:**
```bash
python manage.py migrate
```
5. **Create a superuser (for Admin access):**
```bash
python manage.py createsuperuser
```
6. **Run the server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the blog. Access the admin panel at `http://127.0.0.1:8000/admin/`.

## Acknowledgments
Thanks to the [Django Girls](https://djangogirls.org/) community for the excellent tutorial and resources.