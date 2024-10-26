import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/auth.css'; // Ensure this path is correct
import { useNavigate } from 'react-router-dom';
import Navigation from '../components/Navigation';

const SignUpPage = () => {
  const navigate = useNavigate(); // Initialize useNavigate
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    firstName: '',
    lastName: '',
    profilePicture: null, // Change to null for file input
    bio: ''
  });

  const handleInputChange = (e) => {
    const { name, value, type, files } = e.target;

    // If the input is of type file, set the file instead of the value
    setFormData({ ...formData, [name]: type === 'file' ? files[0] : value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Password validation: must contain at least one letter, one number, and one special character
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    const isPasswordValid = passwordPattern.test(formData.password);

    // Log the form data and password validation result
    // console.log('Form Data:', formData);
    // console.log('Is Password Valid:', isPasswordValid);

    if (!isPasswordValid) {
      alert('Password must be at least 8 characters long and include at least one letter, one number, and one special character.');
      return;
    }

    // Prepare the data to be sent to the API
    const dataToSend = {
      username: formData.username,
      email: formData.email,
      password: formData.password,
      firstName: formData.firstName,
      lastName: formData.lastName,
      bio: formData.bio
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      console.log('API Response:', result);

      // Assuming the sign-up process is successful, navigate to the HomePage
      navigate('/home'); // Replace '/home' with the actual route to your HomePage
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  };

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
                  required
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
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="profilePicture">Profile Picture</label>
                <input
                  type="file"
                  className="form-control"
                  id="profilePicture"
                  name="profilePicture"
                  onChange={handleInputChange}
                  accept=".png, .jpg, .jpeg" // Accept only PNG and JPG files
                  // Optional: make it required if you want to enforce a profile picture upload
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