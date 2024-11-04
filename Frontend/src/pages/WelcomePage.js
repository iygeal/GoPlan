// WelcomePage.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/welcomepage.css';

const WelcomePage = ({ firstName }) => {
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);

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
        <h1 className="welcome-message">Welcome, {firstName}!</h1>
        <button className="create-plan-btn" onClick={handleCreatePlan}>
          Create a Travel Plan
        </button>
        <button className="see-dashboard-btn" onClick={handleSeeDashboard}>
          See Dashboard
        </button>
      </div>
    </div>
  );
};

export default WelcomePage;
