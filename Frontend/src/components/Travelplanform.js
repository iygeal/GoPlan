import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

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

const TravelPlanForm = ({ plan, onSubmit }) => {
  const [state, setState] = useState('');
  const [city, setCity] = useState('');
  const [budget, setBudget] = useState('');
  const [activities, setActivities] = useState('');
  const [accommodationDetails, setAccommodationDetails] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [title, setTitle] = useState('');
  const [dateError, setDateError] = useState('');

  useEffect(() => {
    // Update state when the plan prop changes (for editing)
    if (plan) {
      setState(plan.state);
      setCity(plan.city);
      setBudget(plan.budget.toString());
      setActivities(plan.activities);
      setAccommodationDetails(plan.accommodation_details);
      setStartDate(plan.start_date.split('T')[0]); // Format to yyyy-MM-dd
      setEndDate(plan.end_date.split('T')[0]); // Format to yyyy-MM-dd
      setTitle(plan.title);
    }
  }, [plan]);

  const handleStateChange = (e) => {
    setState(e.target.value);
    setCity('');
  };

  const handleBudgetChange = (e) => {
    const value = e.target.value.replace(/[^0-9]/g, '');
    setBudget(value);
  };

  const validateDates = () => {
    const today = new Date();
    const start = new Date(startDate);
    const end = new Date(endDate);
    
    // Reset date error
    setDateError('');

    if (start < today) {
      setDateError("Start date cannot be in the past.");
      return false;
    }
    if (end < today) {
      setDateError("End date cannot be in the past.");
      return false;
    }
    if (start > end) {
      setDateError("End date cannot be before start date.");
      return false;
    }
    return true;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validateDates()) return; // Only proceed if dates are valid

    const travelPlanData = {
      id: plan?.id || undefined, // Ensure the id is included for updates
      title,
      state,
      city,
      budget: parseInt(budget.replace(/,/g, ''), 10), // Parse budget as integer and remove commas
      activities,
      accommodation_details: accommodationDetails,
      start_date: startDate,
      end_date: endDate,
    };
    onSubmit(travelPlanData);
  };

  return (
    <form className="homepage-form mt-4" onSubmit={handleSubmit}>
      <div className="form-group mb-4">
        <label htmlFor="title" className="form-label">Title</label>
        <input
          type="text"
          className="form-control"
          id="title"
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
        <label htmlFor="budget" className="form-label">Budget (₦)</label>
        <input
          type="text"
          className="form-control"
          id="budget"
          value={budget.toLocaleString()} // Display with commas
          onChange={handleBudgetChange}
          placeholder="Enter your budget"
          required
        />
      </div>

      <div className="form-group mb-4">
        <label htmlFor="activities" className="form-label">Activities</label>
        <textarea
          className="form-control"
          id="activities"
          value={activities}
          onChange={(e) => setActivities(e.target.value)}
          placeholder="Describe activities"
          required
        />
      </div>

      <div className="form-group mb-4">
        <label htmlFor="accommodation" className="form-label">Accommodation</label>
        <textarea
          className="form-control"
          id="accommodation"
          value={accommodationDetails}
          onChange={(e) => setAccommodationDetails(e.target.value)}
          placeholder="Accommodation details"
          required
        />
      </div>

      <div className="form-group mb-4">
        <label htmlFor="startDate" className="form-label">Start Date</label>
        <input
          type="date"
          className="form-control"
          id="startDate"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          required
        />
      </div>

      <div className="form-group mb-4">
        <label htmlFor="endDate" className="form-label">End Date</label>
        <input
          type="date"
          className="form-control"
          id="endDate"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          required
        />
        {dateError && <small className="text-danger">{dateError}</small>}
      </div>

      <button type="submit" className="btn btn-primary">
        {plan ? 'Update Travel Plan' : 'Create Travel Plan'}
      </button>
    </form>
  );
};

export default TravelPlanForm;
