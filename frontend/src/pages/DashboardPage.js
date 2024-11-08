import React, { useEffect, useState, useRef } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/dashboardpage.css'; // Import custom CSS for the dashboard page
import { useNavigate } from 'react-router-dom';
import TravelPlanForm from '../components/Travelplanform'; // Import TravelPlanForm component

const DashboardPage = () => {
  // State variables to manage travel plans, editing state, completed plans, etc.
  const [travelPlans, setTravelPlans] = useState([]);
  const [editingPlanId, setEditingPlanId] = useState(null); // Track the ID of the plan being edited
  const [editedPlan, setEditedPlan] = useState({}); // Store the details of the plan being edited
  const [completedPlans, setCompletedPlans] = useState(new Set()); // Track completed plans by their IDs
  const navigate = useNavigate(); // React Router hook for navigation
  const modalRef = useRef(null); // Reference to modal container for editing plans

  useEffect(() => {
    // Function to fetch travel plans from the server
    const fetchTravelPlans = async () => {
      const accessToken = localStorage.getItem('access_token');
      if (!accessToken) {
        navigate('/login'); // Redirect to login if no access token is found
        return;
      }

      try {
        // Fetch travel plans with authorization header
        const response = await fetch('http://localhost:5000/api/dashboard', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch travel plans');
        }

        const plans = await response.json();
        // Sort plans by creation date in descending order
        plans.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
        setTravelPlans(plans);
      } catch (error) {
        console.error('Error fetching travel plans:', error);
      }
    };

    fetchTravelPlans(); // Initial fetch on component mount
  }, [navigate]);

  const handleDelete = async (planId) => {
    const accessToken = localStorage.getItem('access_token');

    if (window.confirm('Are you sure you want to delete this travel plan?')) {
      try {
        // Send a delete request for the specified plan
        const response = await fetch(`http://localhost:5000/api/dashboard/${planId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });

        if (!response.ok) {
          const responseData = await response.json();
          alert(responseData.error || 'Failed to delete travel plan');
          return;
        }

        // Remove deleted plan from state
        setTravelPlans((prevPlans) => prevPlans.filter((plan) => plan.id !== planId));
        alert('Travel plan deleted successfully!');
      } catch (error) {
        console.error('Error deleting travel plan:', error);
        alert('Error deleting travel plan. Please try again.');
      }
    }
  };

  const handleEdit = (plan) => {
    // Set editing state and populate form with current plan data
    setEditingPlanId(plan.id);
    setEditedPlan({
      ...plan,
      start_date: formatDate(plan.start_date),
      end_date: formatDate(plan.end_date),
    });
  };

  const handleSave = async (updatedPlan) => {
    const accessToken = localStorage.getItem('access_token');
    const planId = editingPlanId;

    // Ensure dates are valid
    const today = new Date();
    const startDate = new Date(updatedPlan.start_date);
    const endDate = new Date(updatedPlan.end_date);

    if (startDate < today) {
      alert("Start date cannot be in the past.");
      return;
    }

    if (endDate < startDate) {
      alert("End date must be after start date.");
      return;
    }

    // Prepare data for updating the plan
    const dataToSend = {
      title: updatedPlan.title,
      state: updatedPlan.state,
      city: updatedPlan.city,
      start_date: updatedPlan.start_date,
      end_date: updatedPlan.end_date,
      activities: updatedPlan.activities,
      budget: updatedPlan.budget,
      accommodation_details: updatedPlan.accommodation_details,
    };

    try {
      // Send a PUT request to update the travel plan
      const response = await fetch(`http://localhost:5000/api/travel-plans/${planId}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      });

      if (!response.ok) {
        const responseData = await response.json();
        alert(responseData.error || 'Failed to update travel plan');
        return;
      }

      // Update the travel plan in state
      setTravelPlans((prevPlans) =>
        prevPlans.map((plan) => (plan.id === planId ? { ...plan, ...dataToSend, updated_at: new Date().toISOString() } : plan))
      );

      setEditingPlanId(null); // Clear editing state
      alert(`Travel plan updated successfully! Edited at: ${new Date().toLocaleString()}`);
    } catch (error) {
      console.error('Error updating travel plan:', error);
      alert('Error updating travel plan. Please try again.');
    }
  };

  const handleChange = (e) => {
    // Handle form input changes during editing
    const { name, value } = e.target;
    setEditedPlan((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleCancelEdit = () => {
    // Cancel editing and clear edited plan data
    setEditingPlanId(null);
    setEditedPlan({});
  };

  useEffect(() => {
    // Detect clicks outside modal to close it when editing
    const handleClickOutside = (e) => {
      if (modalRef.current && !modalRef.current.contains(e.target)) {
        handleCancelEdit();
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const formatDate = (dateString) => {
    // Format date string as yyyy-MM-dd
    const date = new Date(dateString);
    return date.toISOString().split('T')[0];
  };

  const handleToggleComplete = (planId) => {
    // Toggle the completion status of a travel plan
    setCompletedPlans((prevCompleted) => {
      const newCompleted = new Set(prevCompleted);
      if (newCompleted.has(planId)) {
        newCompleted.delete(planId);
      } else {
        newCompleted.add(planId);
      }
      return newCompleted;
    });
  };

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Your Travel Plans</h1>
        <button className="btn btn-secondary mb-3" onClick={() => navigate(-1)}>
          Back
        </button>
      </header>
      <div className="text-center mb-4">
        <button className="btn btn-info" onClick={() => navigate('/home')}>Create Travel Plan</button>
      </div>
      <main>
        <section className="travel-plan-checklist">
          <h2>Checklist for Completed Travels</h2>
          <ul className="list-group mb-3">
            {travelPlans.map((plan) => (
              <li key={plan.id} className="list-group-item d-flex justify-content-between align-items-center">
                <span>{plan.title}</span>
                <input
                  type="checkbox"
                  checked={completedPlans.has(plan.id)}
                  onChange={() => handleToggleComplete(plan.id)}
                />
              </li>
            ))}
          </ul>
        </section>

        <section className="travel-plan-list">
          {travelPlans.length === 0 ? (
            <p>No travel plans found.</p>
          ) : (
            <ul className="list-group">
              {travelPlans.map((plan) => (
                <li key={plan.id} className="list-group-item travel-plan-card">
                  {editingPlanId === plan.id ? (
                    <div ref={modalRef} className="dashboard-form-container">
                      <div className="travel-plan-form">
                        <TravelPlanForm
                          plan={editedPlan}
                          onSubmit={handleSave}
                          onChange={handleChange}
                        />
                        <button className="btn btn-secondary" onClick={handleCancelEdit}>
                          Cancel
                        </button>
                      </div>
                    </div>
                  ) : (
                    <div className="plan-details">
                      <h5>{plan.title}</h5>
                      <p><strong>State:</strong> {plan.state}</p>
                      <p><strong>City:</strong> {plan.city}</p>
                      <p><strong>Budget:</strong> ₦{plan.budget.toLocaleString()}</p>
                      <p><strong>Activities:</strong> {plan.activities}</p>
                      <p><strong>Accommodation:</strong> {plan.accommodation_details}</p>
                      <p><strong>Start Date:</strong> {formatDate(plan.start_date)}</p>
                      <p><strong>End Date:</strong> {formatDate(plan.end_date)}</p>
                      <p><strong>Created At:</strong> {formatDate(plan.created_at)}</p>
                      {plan.updated_at && <p><strong>Updated At:</strong> {formatDate(plan.updated_at)}</p>}
                      <button className="btn btn-primary" onClick={() => handleEdit(plan)}>
                        Edit
                      </button>
                      <button className="btn btn-danger ms-2" onClick={() => handleDelete(plan.id)}>
                        Delete
                      </button>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>
    </div>
  );
};

export default DashboardPage;
