import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/auth.css';
import { useNavigate } from 'react-router-dom';
import Navigation from '../components/Navigation';

const LoginPage = () => {
  const navigate = useNavigate();
  const [error, setError] = useState(null);

  const handleSignUpClick = () => {
    navigate('/signup');
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const loginValue = event.target.elements.login.value;
    const password = event.target.elements.password.value;

    if (!loginValue || !password) {
      alert("Please enter both login credentials and password.");
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: loginValue.includes('@') ? loginValue : null,
          username: !loginValue.includes('@') ? loginValue : null,
          password: password
        })
      });

      if (!response.ok) {
        const errorMessage = await response.text();
        throw new Error(errorMessage || "Invalid login credentials.");
      }

      const result = await response.json();
      console.log('Login successful:', result);

      // Save access token if needed (in localStorage/sessionStorage for persistence)
      localStorage.setItem('access_token', result.access_token);

      navigate('/home'); // Redirect to the profile page upon successful login
    } catch (error) {
      console.error("Login error:", error);
      setError("Invalid login credentials. Please try again.");
    }
  };

  return (
    <div>
      <Navigation />

      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-12 col-md-8 col-lg-6">
            <form className="auth-container" onSubmit={handleSubmit}>
              <h2>Login</h2>
              {error && <div className="alert alert-danger">{error}</div>}
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
