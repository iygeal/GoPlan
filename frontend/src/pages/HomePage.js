import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/homepage.css';
import { useNavigate } from 'react-router-dom';
import TravelPlanForm from '../components/Travelplanform';

const HomePage = () => {
  // Initialize the navigate function for redirecting users to other routes
  const navigate = useNavigate();
  // State to manage dropdown visibility
  const [showDropdown, setShowDropdown] = useState(false);
  // State to store the success message after creating a travel plan
  const [successMessage, setSuccessMessage] = useState('');

  // Check if the user is authenticated when the component mounts
  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    // If no access token is found, redirect to the login page
    if (!accessToken) {
      navigate('/login');
    }
  }, [navigate]);

  // Function to handle form submission for creating a new travel plan
  const handleTravelPlanSubmit = (travelPlanData) => {
    // Send POST request to the backend with the travel plan data
    fetch('/api/travel-plans', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Include the access token in the Authorization header
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
      },
      body: JSON.stringify(travelPlanData),
    })
    .then(response => {
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Travel Plan Created:', data);
      // Display success message upon successful travel plan creation
      setSuccessMessage('Travel plan created successfully!');
      // Redirect to the dashboard after a short delay
      setTimeout(() => {
        navigate('/dashboard');
      }, 2000);
    })
    .catch((error) => {
      console.error('Error creating travel plan:', error);
      // Show an error alert if travel plan creation fails
      alert('There was an error creating your travel plan. Please try again.');
    });
  };

  return (
    <div className="homepage">
      {/* Header section with logo and profile icon */}
      <header className="d-flex justify-content-between align-items-center px-4 py-2">
        <img src="/assets/images/goplanlogo.png" alt="GoPlan Logo" className="logo" />
        
        {/* Profile icon with dropdown for navigation options */}
        <div className="profile-icon" onClick={() => setShowDropdown(!showDropdown)} style={{ cursor: 'pointer' }}>
          <img src="/assets/images/maleuser.png" alt="Profile" />
          {showDropdown && (
            <div className="dropdown-menu">
              <div className="dropdown-item" onClick={() => navigate('/profile')}>Your Profile</div>
              <div className="dropdown-item" onClick={() => navigate('/dashboard')}>Dashboard</div>
              <div className="dropdown-item" onClick={() => navigate('/welcome')}>Welcome</div> {/* Added Welcome option */}
              <div className="dropdown-item" onClick={() => {
                // Logout by removing access token and navigating to login
                localStorage.removeItem('access_token');
                navigate('/login');
              }}>Logout</div>
            </div>
          )}
        </div>
      </header>

      {/* Display success message if a travel plan is successfully created */}
      {successMessage && (
        <div className="alert alert-success text-center mt-3" role="alert">
          {successMessage}
        </div>
      )}

      {/* Main content area with title and travel plan form */}
      <main className="d-flex flex-column align-items-center justify-content-center text-center">
        <h1 className="title">Plan Travel</h1>
        {/* Render the travel plan form and handle submission */}
        <TravelPlanForm onSubmit={handleTravelPlanSubmit} />
      </main>
    </div>
  );
};

export default HomePage;
