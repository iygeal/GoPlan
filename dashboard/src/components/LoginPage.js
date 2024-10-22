import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/Auth.css'; // Ensure this path is correct
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const LoginPage = () => {
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSignUpClick = () => {
    navigate('/signup'); // Navigate to Sign Up page
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form>
        <div className="form-group">
          <label htmlFor="email">Email address</label>
          <input type="email" className="form-control" id="email" placeholder="Enter email" required />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" className="form-control" id="password" placeholder="Password" required />
        </div>
        <button type="submit" className="btn btn-success btn-block">Login</button>
      </form>
      <div className="text-center mt-2">
        <a href="/forgot-password" className="forgot-password">Forgot Password?</a>
      </div>
      <div className="text-center mt-3">
        <p>Don't have an account? <span className="link" onClick={handleSignUpClick}>Sign Up</span></p>
      </div>
    </div>
  );
};

export default LoginPage;
