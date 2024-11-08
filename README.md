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

- **Frontend:** React, JavaScript, HTML, CSS, Bootstrap
- **Backend:** Flask, Python
- **Database:** MySQL
- **Version Control:** Git
- **Deployment:** TBD

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
   - Create a MySQL database.
   - Update `SQLALCHEMY_DATABASE_URI` in `config.py` with your credentials.
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/gotravel_db'
   ```

7. **Run Migrations:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

8. **Start Flask Server:**
   ```bash
   flask run
   ```

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