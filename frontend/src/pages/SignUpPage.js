import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/auth.css';
import { useNavigate } from 'react-router-dom';
import Navigation from '../components/Navigation';

const SignUpPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    firstName: '',
    lastName: '',
    bio: ''
  });
  const [shouldSubmit, setShouldSubmit] = useState(false);
  const [error, setError] = useState('');

  // Handle input change and update formData state
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Form submission handler with password validation
  const handleSubmit = (e) => {
    e.preventDefault();
    setError('');
    
    // Validate password strength
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(formData.password)) {
      alert('Password must be at least 8 characters long and include at least one letter, one number, and one special character.');
      return;
    }

    // Trigger form submission
    setShouldSubmit(true);
  };

  // Effect to submit formData when shouldSubmit is true
  useEffect(() => {
    const submitFormData = async () => {
      const dataToSend = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        first_name: formData.firstName,
        last_name: formData.lastName,
        bio: formData.bio || '' // Optional bio field
      };

      try {
        const response = await fetch('http://localhost:5000/api/users', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(dataToSend)
        });

        // Handle specific errors and responses
        if (response.status === 409) {
          setError('User with this email or username already exists.');
          return;
        } else if (!response.ok) {
          const errorMessage = await response.text();
          throw new Error(`Network response was not ok: ${errorMessage}`);
        }

        // Successful registration; navigate to login page
        const result = await response.json();
        console.log('API Response:', result);
        navigate('/login');
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        setError('An error occurred during registration. Please try again.');
      }
    };

    if (shouldSubmit) {
      submitFormData();
      setShouldSubmit(false);
    }
  }, [shouldSubmit, formData, navigate]);

  const handleLoginClick = () => {
    navigate('/login');
  };

  return (
    <div>
      <Navigation />
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-12 col-md-8 col-lg-6">
            <form className="auth-container" onSubmit={handleSubmit}>
              <h2>Sign Up</h2>
              {error && <div className="alert alert-danger">{error}</div>}
              
              {/* Username Input */}
              <div className="form-group">
                <label htmlFor="username">Username</label>
                <input
                  type="text"
                  className="form-control"
                  id="username"
                  name="username"
                  value={formData.username}
                  onChange={handleInputChange}
                  placeholder="Enter your username"
                  maxLength="25"
                  required
                />
              </div>

              {/* Email Input */}
              <div className="form-group">
                <label htmlFor="email">Email address</label>
                <input
                  type="email"
                  className="form-control"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  placeholder="Enter your email"
                  maxLength="50"
                  required
                />
              </div>

              {/* Password Input */}
              <div className="form-group">
                <label htmlFor="password">Password</label>
                <input
                  type="password"
                  className="form-control"
                  id="password"
                  name="password"
                  value={formData.password}
                  onChange={handleInputChange}
                  placeholder="Enter your password"
                  maxLength="20"
                  required
                />
              </div>

              {/* First Name Input */}
              <div className="form-group">
                <label htmlFor="firstName">First Name</label>
                <input
                  type="text"
                  className="form-control"
                  id="firstName"
                  name="firstName"
                  value={formData.firstName}
                  onChange={handleInputChange}
                  placeholder="Enter your first name"
                  maxLength="25"
                  required
                />
              </div>

              {/* Last Name Input */}
              <div className="form-group">
                <label htmlFor="lastName">Last Name</label>
                <input
                  type="text"
                  className="form-control"
                  id="lastName"
                  name="lastName"
                  value={formData.lastName}
                  onChange={handleInputChange}
                  placeholder="Enter your last name"
                  maxLength="25"
                  required
                />
              </div>

              {/* Bio Input */}
              <div className="form-group">
                <label htmlFor="bio">Bio</label>
                <textarea
                  className="form-control"
                  id="bio"
                  name="bio"
                  value={formData.bio}
                  onChange={handleInputChange}
                  placeholder="Tell us about yourself (Optional)"
                />
              </div>

              {/* Submit Button */}
              <button type="submit" className="btn btn-success btn-block">Sign Up</button>
            </form>

            {/* Login Link */}
            <div className="text-center mt-3">
              <p>Already have an account? <span className="link" onClick={handleLoginClick}>Login</span></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignUpPage;
