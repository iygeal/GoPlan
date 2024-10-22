import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Auth.css'; // Ensure this path is correct
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const SignUpPage = () => {
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to Login page
  };

  return (
    <div className="auth-container">
      <h2>Sign Up</h2>
      <form>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input type="text" className="form-control" id="name" placeholder="Enter your name" required />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email address</label>
          <input type="email" className="form-control" id="email" placeholder="Enter email" required />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" className="form-control" id="password" placeholder="Password" required />
        </div>
        <button type="submit" className="btn btn-success btn-block">Sign Up</button>
      </form>
      <div className="text-center mt-3">
        <p>Already have an account? <span className="link" onClick={handleLoginClick}>Login</span></p>
      </div>
    </div>
  );
};

export default SignUpPage;
