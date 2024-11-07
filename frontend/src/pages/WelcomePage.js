import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/welcomepage.css';

const WelcomePage = () => {
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);
  const [animated, setAnimated] = useState(false);
  const [firstName, setFirstName] = useState(''); // State to hold the first name

  useEffect(() => {
    setAnimated(true); // Trigger animation after component mounts

    // Retrieve first name from local storage
    const storedFirstName = localStorage.getItem('first_name');
    if (storedFirstName) {
      setFirstName(storedFirstName);
    } else {
      // Fallback if no name is stored (can be improved based on your app's logic)
      setFirstName('User');
    }
  }, []);

  const handleCreatePlan = () => {
    navigate('/home');
  };

  const handleSeeDashboard = () => {
    navigate('/dashboard');
  };

  return (
    <div className="welcome-page">
      <header className="d-flex justify-content-between align-items-center px-4 py-2">
        <img src="/assets/images/goplanlogo.png" alt="GoPlan Logo" className="logo" />
        <div className="profile-icon" onClick={() => setShowDropdown(!showDropdown)} style={{ cursor: 'pointer' }}>
          <img src="/assets/images/maleuser.png" alt="Profile" />
          {showDropdown && (
            <div className="dropdown-menu">
              <div className="dropdown-item" onClick={() => navigate('/profile')}>Your Profile</div>
              <div className="dropdown-item" onClick={() => navigate('/dashboard')}>Dashboard</div>
              <div className="dropdown-item" onClick={() => {
                localStorage.removeItem('access_token');
                navigate('/login');
              }}>Logout</div>
            </div>
          )}
        </div>
      </header>

      <div className="welcome-content text-center">
        <h1 className={`welcome-message ${animated ? 'animate' : ''}`}>Welcome, {firstName}!</h1>
        <button className="create-plan-btn" onClick={handleCreatePlan}>
          Create a Travel Plan
        </button>
        <button className="see-dashboard-btn" onClick={handleSeeDashboard}>
          See Dashboard
        </button>
      </div>

      <footer className="bg-light text-center text-lg-start mt-4">
        <div className="container p-4">
          <img src="/assets/images/goplanlogo.png" className="logo my-3" alt="GoPlan Logo" />
          <p>Discover Nigeria like never before with GoPlan. Explore the most visited places, festivals, and more.</p>
        </div>
        <div className="text-center p-3" style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
          © 2024 Copyright:
          <a className="text-dark" href="https://github.com/VictorNalu/GoPlan/"> GoPlan Devs</a>
        </div>
      </footer>
    </div>
  );
};

export default WelcomePage;
