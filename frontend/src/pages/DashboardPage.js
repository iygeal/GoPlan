import React, { useEffect, useState, useRef } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/dashboardpage.css'; // Make sure the CSS is updated accordingly
import { useNavigate } from 'react-router-dom';
import TravelPlanForm from '../components/Travelplanform'; // Adjust the path as needed

const DashboardPage = () => {
  const [travelPlans, setTravelPlans] = useState([]);
  const [editingPlanId, setEditingPlanId] = useState(null);
  const [editedPlan, setEditedPlan] = useState({});
  const [completedPlans, setCompletedPlans] = useState(new Set()); // Track completed plans
  const navigate = useNavigate();
  const modalRef = useRef(null);

  useEffect(() => {
    const fetchTravelPlans = async () => {
      const accessToken = localStorage.getItem('access_token');
      if (!accessToken) {
        navigate('/login'); // Redirect if not authenticated
        return;
      }

      try {
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
        plans.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
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

        setTravelPlans((prevPlans) => prevPlans.filter((plan) => plan.id !== planId));
        alert('Travel plan deleted successfully!');
      } catch (error) {
        console.error('Error deleting travel plan:', error);
        alert('Error deleting travel plan. Please try again.');
      }
    }
  };

  const handleEdit = (plan) => {
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

      setTravelPlans((prevPlans) =>
        prevPlans.map((plan) => (plan.id === planId ? { ...plan, ...dataToSend, updated_at: new Date().toISOString() } : plan))
      );

      setEditingPlanId(null);
      alert(`Travel plan updated successfully! Edited at: ${new Date().toLocaleString()}`);
    } catch (error) {
      console.error('Error updating travel plan:', error);
      alert('Error updating travel plan. Please try again.');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEditedPlan((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleCancelEdit = () => {
    setEditingPlanId(null);
    setEditedPlan({});
  };

  useEffect(() => {
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
    const date = new Date(dateString);
    return date.toISOString().split('T')[0];
  };

  const handleToggleComplete = (planId) => {
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
                      {plan.updated_at && (
                        <p><strong>Edited At:</strong> {formatDate(plan.updated_at)}</p>
                      )}
                      <div className="button-group">
                        <button
                          className="btn btn-info mr-2"
                          onClick={() => handleEdit(plan)}
                        >
                          Edit
                        </button>
                        <button
                          className="btn btn-danger"
                          onClick={() => handleDelete(plan.id)}
                        >
                          Delete
                        </button>
                      </div>
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
