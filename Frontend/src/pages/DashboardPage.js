import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';

const DashboardPage = () => {
  const [travelPlans, setTravelPlans] = useState([]);
  const navigate = useNavigate();

  // Fetch travel plans when the component mounts
  useEffect(() => {
    const fetchTravelPlans = async () => {
      const accessToken = localStorage.getItem('access_token');
      if (!accessToken) {
        navigate('/login'); // Redirect if not authenticated
      }

      try {
        const response = await fetch('http://localhost:5000/api/travel-plans', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${accessToken}`, // Include token if needed
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch travel plans');
        }

        const plans = await response.json();
        setTravelPlans(plans);
      } catch (error) {
        console.error('Error fetching travel plans:', error);
      }
    };

    fetchTravelPlans();
  }, [navigate]);

  const handleDelete = async (planId) => {
    const accessToken = localStorage.getItem('access_token');

    if (window.confirm('Are you sure you want to delete this travel plan?')) {
      try {
        const response = await fetch(`http://localhost:5000/api/travel-plans/${planId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${accessToken}`, // Include token if needed
          },
        });

        if (!response.ok) {
          throw new Error('Failed to delete travel plan');
        }

        // Remove the deleted plan from state
        setTravelPlans((prevPlans) => prevPlans.filter((plan) => plan._id !== planId));
        alert('Travel plan deleted successfully!');
      } catch (error) {
        console.error('Error deleting travel plan:', error);
        alert('Error deleting travel plan. Please try again.');
      }
    }
  };

  return (
    <div className="dashboard">
      <header>
        <h1>Your Travel Plans</h1>
      </header>
      <main>
        {travelPlans.length === 0 ? (
          <p>No travel plans found.</p>
        ) : (
          <ul className="list-group">
            {travelPlans.map((plan) => (
              <li key={plan._id} className="list-group-item">
                <h5>{plan.title}</h5>
                <p>State: {plan.state}</p>
                <p>City: {plan.city}</p>
                <p>Budget: {plan.budget.toLocaleString()}</p>
                <p>Activities: {plan.activities}</p>
                <p>Accommodation: {plan.accommodation}</p>
                <p>Start Date: {new Date(plan.startDate).toLocaleDateString()}</p>
                <p>End Date: {new Date(plan.endDate).toLocaleDateString()}</p>
                <button
                  className="btn btn-info mr-2"
                  onClick={() => navigate(`/travel-plan/${plan._id}`)} // Navigate to view plan details
                >
                  View
                </button>
                <button
                  className="btn btn-danger"
                  onClick={() => handleDelete(plan._id)} // Call delete function
                >
                  Delete
                </button>
              </li>
            ))}
          </ul>
        )}
      </main>
    </div>
  );
};

export default DashboardPage;
