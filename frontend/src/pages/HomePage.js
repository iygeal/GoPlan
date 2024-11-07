import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/homepage.css';
import { useNavigate } from 'react-router-dom';
import TravelPlanForm from '../components/Travelplanform';

const HomePage = () => {
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');

  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
      navigate('/login');
    }
  }, [navigate]);

  const handleTravelPlanSubmit = (travelPlanData) => {
    fetch('/api/travel-plans', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
      },
      body: JSON.stringify(travelPlanData),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Travel Plan Created:', data);
      setSuccessMessage('Travel plan created successfully!');
      setTimeout(() => {
        navigate('/dashboard');
      }, 2000);
    })
    .catch((error) => {
      console.error('Error creating travel plan:', error);
      alert('There was an error creating your travel plan. Please try again.');
    });
  };

  return (
    <div className="homepage">
      <header className="d-flex justify-content-between align-items-center px-4 py-2">
        <img src="/assets/images/goplanlogo.png" alt="GoPlan Logo" className="logo" />
        <div className="profile-icon" onClick={() => setShowDropdown(!showDropdown)} style={{ cursor: 'pointer' }}>
          <img src="/assets/images/maleuser.png" alt="Profile" />
          {showDropdown && (
            <div className="dropdown-menu">
              <div className="dropdown-item" onClick={() => navigate('/profile')}>Your Profile</div>
              <div className="dropdown-item" onClick={() => navigate('/dashboard')}>Dashboard</div>
              <div className="dropdown-item" onClick={() => navigate('/welcome')}>Welcome</div> {/* Added Welcome option */}
              <div className="dropdown-item" onClick={() => {
                localStorage.removeItem('access_token');
                navigate('/login');
              }}>Logout</div>
            </div>
          )}
        </div>
      </header>

      {successMessage && (
        <div className="alert alert-success text-center mt-3" role="alert">
          {successMessage}
        </div>
      )}

      <main className="d-flex flex-column align-items-center justify-content-center text-center">
        <h1 className="title">Plan Travel</h1>
        <TravelPlanForm onSubmit={handleTravelPlanSubmit} />
      </main>
    </div>
  );
};

export default HomePage;
