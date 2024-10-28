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

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordPattern.test(formData.password)) {
      alert('Password must be at least 8 characters long and include at least one letter, one number, and one special character.');
      return;
    }
    setShouldSubmit(true);
  };

  useEffect(() => {
    const submitFormData = async () => {
      // Prepare the data without profile picture for JSON-only submission
      const dataToSend = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        first_name: formData.firstName,
        last_name: formData.lastName,
        bio: formData.bio
      };

      try {
        const response = await fetch('http://localhost:5000/api/users', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(dataToSend)
        });

        if (!response.ok) {
          const errorMessage = await response.text();
          throw new Error(`Network response was not ok: ${errorMessage}`);
        }

        const result = await response.json();
        console.log('API Response:', result);
        navigate('/home'); // Redirect to HomePage after successful registration
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
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
                />
              </div>
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
                />
              </div>
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
              <button type="submit" className="btn btn-success btn-block">Sign Up</button>
            </form>
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
