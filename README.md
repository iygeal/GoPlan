# GoPlan Web App

## Introduction

**GoPlan** is an all-in-one travel planning web application that allows users to explore destinations, create and manage travel plans, keep track of checklists, and set budgets. With easy-to-use features for saving and editing travel details, users can conveniently plan and organize their trips.

## Features

### User Authentication

- **Sign Up:** Users can register by providing their name, email, username, and password.
- **Login:** Users can log in using their email or username and password.
- **Profile Management:** Users can edit profile details, including username and email.
- **Logout:** Provides a secure logout option.
- **Account Deletion:** Users can delete their accounts and remove all associated data.

### Travel Plan Management

- **Location Search:** Users can search for destinations by state.
- **Create Travel Plans:** Users can set up travel plans with details such as destination and travel date.
- **Budget Management:** Allows users to set budgets for each travel plan.
- **Save Plan:** Travel plans can be saved to the user’s profile.
- **Checklist of Travels:** Users can mark travels as completed.

### Travel Plan Actions

- **Edit Travel Plans:** Users can update existing travel plans.
- **Delete Travel Plans:** Users can remove travel plans they no longer need.

### Additional Features

- **Profile Dashboard:** Dashboard for managing saved plans and checklists.
- **Responsive Design:** Optimized for usability on multiple devices.

## Technologies Used

## **Backend:**

- **Python 3:** The core programming language.
- **Flask:** The main web framework for building the backend API.
- **Flask-SQLAlchemy:** Used as the ORM for database interactions.
- **MySQL:** The main database for storing application data.
- **SQLite:** Used as an in-memory database for testing.
- **JWT (JSON Web Tokens):** For secure user authentication.
- **Flasgger:** To generate API documentation.
- **Flask-CORS:** To manage cross-origin requests.
- **Flask-Migrate:** For database migrations.

## **Frontend:**

React, JavaScript, HTML, CSS, Bootstrap

- **Version Control:** Git

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/VictorNalu/GoPlan.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd GoPlan
   ```

### Backend Setup

**Pre-requisites:**

- Python 3.10 or higher
- MySQL
- pip
- Set up MySQL credentials, setting a password for the root user, which will be referenced in a .env file for the project.

Run below commands to install essential development tools and MySQL libraries required to compile and link dependencies like mysqlclient for the GoPlan backend:

```bash
sudo apt update
sudo apt install pkg-config libmysqlclient-dev build-essential
```

3. **Navigate to the Backend Directory:**
   ```bash
   cd backend
   ```
4. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
5. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Configure MySQL Database:**

   - Create a file in the backend/ directory named .env to manage environment variables.
   - Add the following variables to the .env file:

     - GO_PLAN_USER=mysql-username
     - GO_PLAN_MYSQL_PWD=mysql-password
     - GO_PLAN_MYSQL_DB=database-name
     - GO_PLAN_MYSQL_HOST=localhost
     - ROOT_MYSQL_PWD=mysql-root-password
     - JWT_SECRET_KEY=jwt-secret-key
     - JWT_ACCESS_TOKEN_EXPIRES=seconds

     **_NB: Ensure to replace the values for these variables with your desired credentials.
     For the ROOT_MYSQL_PWD environment variable, the value MUST match your MySQL root password._**

   - From the backend directory, create the database credentials for the app using a script we have implemented for it.
     Run: `python3 scripts/setup_db.py`
     - If everything goes well, the message **_"Database and user setup complete."_** shall be logged to the console.

7. **Run Database Upgrades:**

   ```bash
   flask db upgrade
   ```

8. **Start Flask Server:**

   ```bash
   flask run
   ```

   - The backend server will now be running at http://127.0.0.1:5000

   ## Swagger Documentation
   - Proper documentation on how to access various endpoints of the GoPlan API can be found on http://localhost:5000/apidocs/ once the server is running.
   - You can also test the endpoints via the Swagger UI at http://localhost:5000/apidocs/

   ## Running Tests

   - Ensure you're in the project’s backend/ directory.
   - Activate the virtual environment if it's not active.
   - Run all tests: `python3 -m unittest discover tests`

### Frontend Setup

9. **Navigate to the Frontend Directory:**

   ```bash
   cd frontend
   ```

10. **Install Node Version 16:**

```bash
nvm install 16
nvm use 16
```

11. **Install Frontend Dependencies:**

    ```bash
    npm install
    ```

12. **Start React Development Server:**
    ```bash
    npm start
    ```

## Usage

1. **Register or Log In:** Start by signing up or logging in.
2. **Search Destinations:** Use the search bar to find destinations by state.
3. **Create Travel Plans:** Add destinations, set travel dates, and allocate budgets.
4. **Save Plans:** Store your travel plans in your profile.
5. **Edit/Delete Plans:** Modify or remove plans as needed.
6. **Delete Account:** Remove your account and all associated data.

## Folder Structure

```
GoPlan/
│
├── backend/                # Flask backend
│   ├── app/                # Core application files
│   ├── migrations/         # Database migrations
│   ├── config.py           # Flask configuration
│   └── requirements.txt    # Python dependencies
│
├── frontend/               # React frontend
│   ├── src/                # React components
│   ├── public/             # Public files (e.g., index.html)
│   └── package.json        # Frontend dependencies
│
└── README.md               # Project documentation
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License.
