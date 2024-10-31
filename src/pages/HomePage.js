import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/homepage.css';
import { useNavigate } from 'react-router-dom';

const statesAndCities = {
  Abia: ['Aba', 'Umuahia', 'Ohafia', 'Arochukwu'],
  Adamawa: ['Yola', 'Mubi', 'Jimeta', 'Numan'],
  AkwaIbom: ['Uyo', 'Ikot Ekpene', 'Eket', 'Oron'],
  Anambra: ['Awka', 'Onitsha', 'Nnewi', 'Ekwulobia'],
  Bauchi: ['Bauchi', 'Azare', 'Misau', 'Jama’are'],
  Bayelsa: ['Yenagoa', 'Brass', 'Ogbia', 'Sagbama'],
  Benue: ['Makurdi', 'Gboko', 'Otukpo', 'Katsina-Ala'],
  Borno: ['Maiduguri', 'Bama', 'Dikwa', 'Konduga'],
  CrossRiver: ['Calabar', 'Ikom', 'Obudu', 'Ogoja'],
  Delta: ['Asaba', 'Warri', 'Sapele', 'Ughelli'],
  Ebonyi: ['Abakaliki', 'Afikpo', 'Onueke', 'Ikwo'],
  Edo: ['Benin City', 'Ekpoma', 'Auchi', 'Irrua'],
  Ekiti: ['Ado-Ekiti', 'Ikere', 'Iworoko', 'Iyin Ekiti'],
  Enugu: ['Enugu', 'Nsukka', 'Awgu', 'Oji River'],
  Gombe: ['Gombe', 'Kaltungo', 'Dukku', 'Deba'],
  Imo: ['Owerri', 'Orlu', 'Okigwe', 'Mbaise'],
  Jigawa: ['Dutse', 'Hadejia', 'Kazaure', 'Gumel'],
  Kaduna: ['Kaduna', 'Zaria', 'Kafanchan', 'Saminaka'],
  Kano: ['Kano', 'Wudil', 'Dawakin Tofa', 'Bichi'],
  Katsina: ['Katsina', 'Daura', 'Funtua', 'Malumfashi'],
  Kebbi: ['Birnin Kebbi', 'Argungu', 'Yauri', 'Zuru'],
  Kogi: ['Lokoja', 'Okene', 'Kabba', 'Idah'],
  Kwara: ['Ilorin', 'Offa', 'Patigi', 'Jebba'],
  Lagos: ['Ikeja', 'Badagry', 'Ikorodu', 'Epe'],
  Nasarawa: ['Lafia', 'Keffi', 'Akwanga', 'Nasarawa'],
  Niger: ['Minna', 'Suleja', 'Kontagora', 'Bida'],
  Ogun: ['Abeokuta', 'Ijebu-Ode', 'Sango-Ota', 'Shagamu'],
  Ondo: ['Akure', 'Owo', 'Ondo Town', 'Ikare'],
  Osun: ['Oshogbo', 'Ile-Ife', 'Ilesa', 'Ede'],
  Oyo: ['Ibadan', 'Ogbomoso', 'Oyo Town', 'Iseyin'],
  Plateau: ['Jos', 'Barkin Ladi', 'Pankshin', 'Shendam'],
  Rivers: ['Port Harcourt', 'Bonny', 'Omoku', 'Opobo'],
  Sokoto: ['Sokoto', 'Tambuwal', 'Bodinga', 'Gwadabawa'],
  Taraba: ['Jalingo', 'Wukari', 'Bali', 'Gembu'],
  Yobe: ['Damaturu', 'Potiskum', 'Gashua', 'Nguru'],
  Zamfara: ['Gusau', 'Kaura Namoda', 'Talata Mafara', 'Maru'],
  Abuja: ['Garki', 'Asokoro', 'Maitama', 'Wuse'],
};

const HomePage = () => {
  const [state, setState] = useState('');
  const [city, setCity] = useState('');
  const [budget, setBudget] = useState('');
  const [activities, setActivities] = useState('');
  const [accommodation, setAccommodation] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [title, setTitle] = useState(''); // New state for title
  const [showDropdown, setShowDropdown] = useState(false);
  const navigate = useNavigate();

  // Check if the user is authenticated
  useEffect(() => {
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
      // Redirect to login page if not authenticated
      navigate('/login');
    }
  }, [navigate]);

  const handleStateChange = (e) => {
    setState(e.target.value);
    setCity(''); // Reset city when state changes
  };

  const handleBudgetChange = (e) => {
    const value = e.target.value.replace(/[^0-9]/g, ''); // Remove non-numeric characters
    setBudget(value.replace(/\B(?=(\d{3})+(?!\d))/g, ',')); // Format with commas
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Prepare the travel plan data
    const travelPlanData = {
      title, // Include title in the travel plan data
      state,
      city,
      budget: parseInt(budget.replace(/,/g, ''), 10), // Convert to integer
      activities,
      accommodation,
      startDate,
      endDate,
    };

    try {
      const response = await fetch('http://localhost:5000/api/travel-plans', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`, // Include token if needed
        },
        body: JSON.stringify(travelPlanData),
      });

      if (!response.ok) {
        const errorMessage = await response.text();
        throw new Error(errorMessage || 'Failed to save travel plan.');
      }

      // Optionally handle response to update UI or notify user
      alert('Travel plan saved successfully!');

      // Redirect or navigate to the dashboard
      navigate('/dashboard'); // Assuming you want to navigate to the dashboard

    } catch (error) {
      console.error('Error saving travel plan:', error);
      alert('Error saving travel plan. Please try again.');
    }
  };

  return (
    <div className="homepage">
      <header className="d-flex justify-content-between align-items-center px-4 py-2">
        <img src="/assets/images/goplanlogo.png" alt="GoPlan Logo" className="logo" />
        <div className="profile-icon" onClick={() => setShowDropdown(!showDropdown)}>
          <img src="/assets/images/maleuser.png" alt="Profile" />
          {showDropdown && (
            <div className="dropdown-menu">
              <div className="dropdown-item" onClick={() => navigate('/profile')}>Your Profile</div>
              <div className="dropdown-item" onClick={() => navigate('/dashboard')}>Dashboard</div>
              <div className="dropdown-item" onClick={() => {
                // Implement logout logic here
                // For example, clear the authentication state
                localStorage.removeItem('access_token'); // Clear the access token
                navigate('/login');
              }}>Logout</div>
            </div>
          )}
        </div>
      </header>

      <main className="d-flex flex-column align-items-center justify-content-center text-center">
        <h1 className="text-success">Plan Travel</h1>
        <form className="homepage-form mt-4" onSubmit={handleSubmit}>
          {/* Title Field */}
          <div className="form-group mb-4">
            <label htmlFor="title" className="form-label">Title</label>
            <input
              type="text"
              className="form-control"
              id="title"
              name="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter travel plan title"
              required
            />
          </div>

          <div className="form-group mb-4">
            <label htmlFor="state" className="form-label">State</label>
            <select
              className="form-control"
              id="state"
              name="state"
              value={state}
              onChange={handleStateChange}
              required
            >
              <option value="" disabled>Select State</option>
              {Object.keys(statesAndCities).map((state) => (
                <option key={state} value={state}>{state}</option>
              ))}
            </select>
          </div>

          <div className="form-group mb-4">
            <label htmlFor="city" className="form-label">City</label>
            <select
              className="form-control"
              id="city"
              name="city"
              value={city}
              onChange={(e) => setCity(e.target.value)}
              required
              disabled={!state}
            >
              <option value="" disabled>Select City</option>
              {state && statesAndCities[state].map((city) => (
                <option key={city} value={city}>{city}</option>
              ))}
            </select>
          </div>

          <div className="form-group mb-4">
            <label htmlFor="budget" className="form-label">Budget</label>
            <input
              type="text"
              className="form-control"
              id="budget"
              name="budget"
              value={budget}
              onChange={handleBudgetChange}
              placeholder="Enter budget amount"
              required
            />
          </div>

          <div className="form-group mb-4">
            <label htmlFor="activities" className="form-label">Activities</label>
            <textarea
              className="form-control"
              id="activities"
              name="activities"
              value={activities}
              onChange={(e) => setActivities(e.target.value)}
              placeholder="Enter planned activities"
              required
            />
          </div>

          <div className="form-group mb-4">
            <label htmlFor="accommodation" className="form-label">Accommodation</label>
            <input
              type="text"
              className="form-control"
              id="accommodation"
              name="accommodation"
              value={accommodation}
              onChange={(e) => setAccommodation(e.target.value)}
              placeholder="Enter accommodation details"
              required
            />
          </div>

          <div className="form-group mb-4">
            <label htmlFor="start-date" className="form-label">Start Date</label>
            <input
              type="date"
              className="form-control"
              id="start-date"
              name="start-date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              required
            />
          </div>

          <div className="form-group mb-4">
            <label htmlFor="end-date" className="form-label">End Date</label>
            <input
              type="date"
              className="form-control"
              id="end-date"
              name="end-date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-success">Save Travel Plan</button>
        </form>
      </main>
    </div>
  );
};

export default HomePage;
