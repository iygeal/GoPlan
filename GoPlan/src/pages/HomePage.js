import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/homepage.css';
// import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  // const navigate = useNavigate();

  return (
    <div className="homepage">
      <header className="d-flex justify-content-between align-items-center px-4 py-2">
        <img src="/assets/images/goplanlogo.png" alt="GoPlan Logo" className="logo" />
        <div className="profile-icon">
          <img src="/assets/images/maleuser.png" alt="Profile" />
        </div>
      </header>
      <main className="d-flex flex-column align-items-center justify-content-center text-center">
        <h1 className="text-success">Plan Travel</h1>
        <form className="homepage-form mt-4">
          <div className="form-group mb-4">
            <label htmlFor="destination" className="form-label">Destination?</label>
            <input
              type="text"
              className="form-control"
              id="destination"
              name="destination"
              placeholder="e.g. Abia, Akwa"
              required
            />
          </div>
          <div className="form-group mb-4">
            <label htmlFor="travel-schedule" className="form-label">Travel Schedule</label>
            <div className="d-flex gap-3">
              <input
                type="date"
                className="form-control"
                id="start-date"
                name="start"
                required
              />
              <input
                type="date"
                className="form-control"
                id="end-date"
                name="end"
                required
              />
            </div>
          </div>
          <button type="submit" className="btn btn-success btn-block mt-3">Create Plan</button>
        </form>
      </main>
      <footer className="text-center py-3">
        <p>Copyright © 2024. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
