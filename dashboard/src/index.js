import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom/client'; // Ensure you import from 'react-dom/client'
import HomePage from './pages/HomePage'; // Adjust path if needed

const root = ReactDOM.createRoot(document.getElementById('root')); // Create the root element

root.render(
  <React.StrictMode>
    <HomePage /> {/* Use HomePage component here */}
  </React.StrictMode>
);
