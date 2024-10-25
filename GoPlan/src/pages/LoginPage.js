import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/auth.css'; // Ensure this path is correct
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import Navigation from '../components/Navigation'; // Import Navigation component

const LoginPage = () => {
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSignUpClick = () => {
    navigate('/signup'); // Navigate to Sign Up page
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const loginValue = event.target.elements.login.value;
    const password = event.target.elements.password.value;

    // Add form validation and API call logic here
    // Example: Validate login value as either email or username
    if (!loginValue || !password) {
      alert("Please enter both login credentials and password.");
      return;
    }

    // Perform login logic (API request or authentication check)
    console.log("Logging in with:", { loginValue, password });

    // Example: Redirect to homepage on successful login
    // This should be replaced with actual authentication logic
    if (loginValue === "user@example.com" && password === "password123") {
      navigate('/HomePage'); // Redirect to homepage
    } else {
      alert("Invalid login credentials.");
    }
  };

  return (
    <div>
      <Navigation /> {/* Include Navigation component */}

      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-12 col-md-8 col-lg-6">
            <form className="auth-container" onSubmit={handleSubmit}>
              <h2>Login</h2>
              <div className="form-group">
                <label htmlFor="login">Email or Username</label>
                <input
                  type="text"
                  className="form-control"
                  id="login"
                  name="login"
                  placeholder="Enter email or username"
                  maxLength="50"
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="password">Password</label>
                <input
                  type="password"
                  className="form-control"
                  id="password"
                  name="password"
                  placeholder="Password"
                  maxLength="20"
                  required
                />
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
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
