import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/SignUpPage';
import HomePage from './pages/HomePage';
import ProfilePage from './pages/ProfilePage';
import DashboardPage from './pages/DashboardPage';
import WelcomePage from './pages/WelcomePage';

const root = ReactDOM.createRoot(document.getElementById('root'));

const App = () => {
  const [user, setUser] = useState(null); // State to hold the user data

  const handleLogin = (userData) => {
    setUser(userData); // Update user state upon login
    localStorage.setItem('first_name', userData.first_name); // Store the first name in localStorage
  };

  useEffect(() => {
    const storedFirstName = localStorage.getItem('first_name');
    if (storedFirstName) {
      setUser({ first_name: storedFirstName });
    }
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<LoginPage onLogin={handleLogin} />} />
        <Route path="/signup" element={<SignUpPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/welcome" element={<WelcomePage firstName={user?.first_name} />} /> {/* Use user state */}
      </Routes>
    </Router>
  );
};

root.render(
  <React.StrictMode>
    <App /> {/* Wrap the Routes in the App component to manage state */}
  </React.StrictMode>
);
