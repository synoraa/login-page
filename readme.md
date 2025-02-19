# [Login Page](https://login-page-o5nj.onrender.com)

# Flask Login Page

This is a simple **Flask-based login page** where users can register by providing their **username, email, and password**. After successful registration, a list of all registered accounts is displayed.

## Features
- User registration with **username, email, and password**.
- Displays a list of **all registered users** after form submission.
- Built using **Flask** with basic form handling.

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-login-app.git
   cd flask-login-app
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install flask
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open the browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## File Structure
```
flask-login-app/
│── app.py           # Main Flask application
│── templates/
│   ├── index.html   # Registration form
│   ├── users.html   # Displays list of registered users
│── static/
│   ├── style.css    # Optional styling
│── README.md        # Project documentation
```

## How It Works
1. The user enters a **username, email, and password**.
2. After submission, the account is stored in a **list or database**.
3. The list of **all registered users** is displayed on the screen.

## Technologies Used
- **Flask** (Backend Framework)
- **HTML & CSS** (Frontend UI)

## Future Enhancements
- Store user data in **SQLite/MySQL** instead of a list.
- Add **password hashing** for security.
- Implement **login/logout** functionality.

## License
This project is open-source and available under the **MIT License**.

