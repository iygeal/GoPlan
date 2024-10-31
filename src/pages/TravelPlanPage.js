import React, { useState } from 'react';
import '../styles/travelplanpage.css'; // Assuming you have some existing styles in home.css
import axios from 'axios'; // For API calls

const TravelPlanPage = () => {
  const [planName, setPlanName] = useState("Plan 1");
  const [isSaved, setIsSaved] = useState(false);

  // Handler to update plan name
  const handlePlanNameChange = (e) => {
    setPlanName(e.target.value);
  };

  // Handler to save the travel plan
  const handleSavePlan = async () => {
    const confirmSave = window.confirm("Do you want to save this travel plan?");
    if (confirmSave) {
      try {
        // Replace with your backend endpoint URL
        const response = await axios.post('/api/saveTravelPlan', {
          name: planName,
          date: new Date(), // You can customize this as needed
          // Other data you might want to send
        });

        if (response.status === 200) {
          alert("Travel plan saved successfully!");
          setIsSaved(true);
          // Here you can update the dashboard or reload the user’s saved plans
        }
      } catch (error) {
        console.error("Error saving travel plan:", error);
        alert("Failed to save the travel plan. Please try again.");
      }
    }
  };

  return (
    <div className="travel-plan-page">
      <div className="sidebar">
        <button className="overview-button">Overview</button>
        <button>Explore</button>
        <button>Travel Date(s)</button>
        <button>Expenses</button>
        <button className="hide-button">Hide</button>
      </div>

      <div className="main-content">
        <div className="header">
          <div className="logo">Gotravel</div>
          <div className="icons">
            <span>undo</span>
            <span>redo</span>
          </div>
        </div>

        <div className="plan-card">
          <input
            type="text"
            value={planName}
            onChange={handlePlanNameChange}
            className="plan-name-input"
          />
          <span className="travel-date">Travel Date</span>
          <button className="save-icon" onClick={handleSavePlan}>Save</button>
        </div>

        <div className="content-section">
          <h2>Explore</h2>
          {/* Content for Explore Section */}
          <div className="image-cards">
            <div className="image-card"> {/* Repeat as needed */}
              <img src="image1.jpg" alt="Place 1" />
              <p>Lorem ipsum dolor sit amet...</p>
            </div>
          </div>
          <button className="add-note-button">Add note</button>
        </div>

        <div className="daily-plan">
          <h2>Daily Plan</h2>
          <div>
            <h3>1st Date</h3>
            <button className="add-place-button">Add place</button>
            <button className="add-note-button">Add note</button>
          </div>
          <div>
            <h3>2nd Date</h3>
            <button className="add-place-button">Add place</button>
            <button className="add-note-button">Add note</button>
          </div>
        </div>

        <div className="expenses-section">
          <h2>Expenses</h2>
          <button className="add-expense-button">Add Item</button>
        </div>
      </div>

      <footer className="footer">
        <p>Copyright © 2024. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default TravelPlanPage;
