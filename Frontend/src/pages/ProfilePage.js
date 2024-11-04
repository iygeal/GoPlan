import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfilePage = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [editMode, setEditMode] = useState(false);
    const [updatedUser, setUpdatedUser] = useState({});
    const [loadingSave, setLoadingSave] = useState(false); // State to handle loading during save

    useEffect(() => {
        const getProfileData = async () => {
            try {
                const token = localStorage.getItem('access_token');
                if (!token) {
                    throw new Error("Authorization token is missing.");
                }

                const userId = JSON.parse(atob(token.split('.')[1])).sub;
                const response = await axios.get(`http://localhost:5000/api/users/${userId}`, {
                    headers: { Authorization: `Bearer ${token}` },
                });

                setUser(response.data);
                setUpdatedUser(response.data); // Initialize updatedUser with current data
            } catch (err) {
                console.error("Error fetching user data:", err);
                setError("Failed to load user data. Please try again.");
            } finally {
                setLoading(false);
            }
        };

        getProfileData();
    }, []);

    const handleEditToggle = () => {
        setEditMode(!editMode);
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setUpdatedUser((prev) => ({ ...prev, [name]: value }));
    };

    const handleSaveChanges = async () => {
        setLoadingSave(true); // Start loading state
        try {
            const token = localStorage.getItem('access_token');
            const userId = JSON.parse(atob(token.split('.')[1])).sub;

            // Create a new object without unwanted keys
            const { id, created_at, updated_at, __class__, ...filteredUser } = updatedUser; // Filter out unwanted properties

            console.log("Updating user with data:", filteredUser); // Log the filtered data to be sent

            const response = await axios.put(`http://localhost:5000/api/users/${userId}`, filteredUser, {
                headers: { Authorization: `Bearer ${token}` },
            });

            console.log("Update response:", response.data); // Log the response

            // Update the local user state with the new data
            setUser(prevUser => ({ ...prevUser, ...filteredUser })); // Merge updated fields with the existing user data
            setEditMode(false);
            setError(null); // Clear any previous error
        } catch (err) {
            console.error("Error updating user data:", err.response ? err.response.data : err);
            setError("Failed to update user data. Please try again.");
        } finally {
            setLoadingSave(false); // End loading state
        }
    };

    const handleDeleteAccount = async () => {
        const confirmDelete = window.confirm("Are you sure you want to delete your account? This action cannot be undone.");
        if (!confirmDelete) return;

        try {
            const token = localStorage.getItem('access_token');
            const userId = JSON.parse(atob(token.split('.')[1])).sub;

            await axios.delete(`http://localhost:5000/api/users/${userId}`, {
                headers: { Authorization: `Bearer ${token}` },
            });

            localStorage.removeItem('access_token');
            window.location.href = '/'; // Redirect to homepage after deletion
        } catch (err) {
            console.error("Error deleting account:", err);
            setError("Failed to delete account. Please try again.");
        }
    };

    if (loading) {
        return <div>Loading user data...</div>;
    }

    if (error) {
        return <div className="alert alert-danger">{error}</div>; // Improved error display
    }

    return (
        <div>
            <h1>Profile Page</h1>
            {user ? (
                <div>
                    <h2>User Details</h2>
                    {editMode ? (
                        <>
                            <div>
                                <strong>Username:</strong>
                                <input type="text" name="username" value={updatedUser.username} onChange={handleInputChange} />
                            </div>
                            <div>
                                <strong>Email:</strong>
                                <input type="email" name="email" value={updatedUser.email} onChange={handleInputChange} />
                            </div>
                            <div>
                                <strong>First Name:</strong>
                                <input type="text" name="first_name" value={updatedUser.first_name} onChange={handleInputChange} />
                            </div>
                            <div>
                                <strong>Last Name:</strong>
                                <input type="text" name="last_name" value={updatedUser.last_name} onChange={handleInputChange} />
                            </div>
                            <div>
                                <strong>Bio:</strong>
                                <textarea name="bio" value={updatedUser.bio} onChange={handleInputChange}></textarea>
                            </div>
                            <button onClick={handleSaveChanges} disabled={loadingSave}>
                                {loadingSave ? 'Saving...' : 'Save Changes'}
                            </button>
                            <button onClick={handleEditToggle}>Cancel</button>
                        </>
                    ) : (
                        <>
                            <p><strong>Username:</strong> {user.username}</p>
                            <p><strong>Email:</strong> {user.email}</p>
                            <p><strong>Full Name:</strong> {user.first_name} {user.last_name}</p>
                            <p><strong>Bio:</strong> {user.bio}</p>
                            <button onClick={handleEditToggle}>Edit Profile</button>
                            <button onClick={handleDeleteAccount}>Delete Account</button>
                        </>
                    )}
                </div>
            ) : (
                <p>No user data available.</p>
            )}
        </div>
    );
};

export default ProfilePage;