# Flask Web Form Project

## Overview
This project is a simple Flask-based web application that serves a form for collecting a user's name and email. The form is built using HTML and styled with Flowbite (Tailwind CSS component library). Upon form submission, the server processes the input.

## Features
- Simple web form to collect user information (name and email).
- Form validation ensuring all fields are filled.
- Server-side processing using Flask.
- Styled with Flowbite and responsive design using Tailwind CSS.
- Dark and light theme support.

## Requirements
- Python 3.x
- Flask 2.x or later
- Tailwind CSS (via CDN)
- Flowbite (via CDN)

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Saf2004/lab-requirement-2
   cd lab-requirement-2
   ```

2. **Set Up Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3**Access the Application**
   The app will be running locally at:
   ```
   http://0.0.0.0:8000
   ```


### `app.py` (Main Application)
This file contains the core Flask application that serves the form and handles the POST request.

### `templates/index.html` (Form)
The HTML form is located in the `templates` folder. Flask's Jinja2 templating system is used to serve this HTML file.

### `static/main.js` (JavaScript)
This file handles any frontend JavaScript functionality for the form (e.g., form validation, interactivity).


```bash
pip install flask
flask run --host 0.0.0.0 --port 8000
```


