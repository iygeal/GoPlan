// WelcomePage.js
import React from 'react';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/welcomepage.css';

const WelcomePage = ({ firstName }) => {
  const navigate = useNavigate();

  const handleCreatePlan = () => {
    navigate('/home');
  };

  return (
    <div className="welcome-page">
      <div className="welcome-content">
        <h1 className="welcome-message">Welcome, {firstName}!</h1>
        <button className="create-plan-btn" onClick={handleCreatePlan}>
          Create a Travel Plan
        </button>
      </div>
    </div>
  );
};

export default WelcomePage;
