# Goplan Web App

## Introduction

**Goplan** is a full-stack travel booking web application that allows users to explore travel destinations, plan trips, manage travel checklists, and budget for activities. Users can create an account, save their travel plans, and manage them conveniently from their profile.

## Features

### User Authentication
- **Sign Up:** Users can create an account by providing their name, email, and username.
- **Login:** Users can log in with either their email or username and password.
- **Profile Management:** Users can edit their profile details, such as their profile photo, username, and email.
- **Logout:** Users can securely log out of their account.
- **Account Deletion:** Users can permanently delete their account, which removes all associated data.

### Travel Plan Management
- **Search for Locations:** Users can search for travel destinations by name of place or festival.
- **Create Travel Plans:** Users can create a travel plan by specifying the destination and the planned travel date.
- **Add Checklists:** For each plan, users can add a list of places to visit and activities to do.
- **Edit/Delete Checklists:** Users can modify or remove items from the checklist.
- **Budgeting:** Users can add and manage their budget for each travel plan.
- **Save Plan:** Travel plans can be saved under the user’s profile for future reference.
- **View History:** Users can access a history of locations they’ve searched for.

### Travel Plan Actions
- **Edit Travel Plans:** Users can edit their saved travel plans (e.g., change the destination, date, checklist, or budget).
- **Delete Travel Plans:** Users can remove travel plans they no longer need.

### Other Features
- **Profile Dashboard:** Users have a dashboard where they can view and manage their saved travel plans and checklists.
- **Search History:** Users can see the locations they have searched for in the past.
- **Responsive Design:** The app is designed to be user-friendly across multiple devices.

## Technologies Used

- **Frontend:** React, JavaScript, HTML, CSS
- **Backend:** Flask, Python
- **Database:** MySQL
- **Version Control:** Git
- **Deployment:** TBD

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/VictorNalu/GoPlan.git
   ```
2. **Navigate to the Project Directory:**
   ```
   cd gotravel
   ```

### Backend Setup

3. **Create and activate a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
4. **Install the required Python packages:**
   ```
   pip install -r requirements.txt
   ```
5. **Set up the MySQL database:**
   - Create a database in MySQL for your app.
   - In the `config.py` file, update the `SQLALCHEMY_DATABASE_URI` with your MySQL credentials and database name.
   ```
   SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/gotravel_db'
   ```

6. **Run database migrations:**
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. **Run the Flask server:**
   ```
   flask run
   ```

### Frontend Setup

8. **Navigate to the frontend directory:**
   ```
   cd frontend
   ```

9. **Install frontend dependencies:**
   ```
   npm install
   ```

10. **Run the React development server:**
    ```
    npm start
    ```

## Usage

1. **Sign Up or Log In:** Start by signing up or logging in to create an account.
2. **Search Destinations:** Use the search bar to find destinations or festivals.
3. **Create Travel Plans:** Once a destination is selected, create a travel plan by adding a date and setting a budget.
4. **Manage Checklists:** Add places and activities to your checklist and modify or delete them as needed.
5. **Save Your Plan:** Your travel plans can be saved under your profile.
6. **View Search History:** You can access the list of places you've searched for.
7. **Edit/Delete Plans:** Modify or remove your travel plans as needed.
8. **Delete Account:** You can delete your account.

## Folder Structure

```
gotravel/
│
├── backend/                # Flask backend
│   ├── app/                # Core app folder
│   ├── migrations/         # Database migrations
│   ├── config.py           # Flask configurations
│   └── requirements.txt    # Python dependencies
│
├── frontend/               # React frontend
│   ├── src/                # React components
│   ├── public/             # Public files (index.html)
│   └── package.json        # Frontend dependencies
│
└── README.md               # Project documentation
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License.
