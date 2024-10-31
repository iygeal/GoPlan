import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfilePage = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [editMode, setEditMode] = useState(false);
    const [updatedUser, setUpdatedUser] = useState({});

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
        try {
            const token = localStorage.getItem('access_token');
            const userId = JSON.parse(atob(token.split('.')[1])).sub;

            await axios.put(`http://localhost:5000/api/users/${userId}`, updatedUser, {
                headers: { Authorization: `Bearer ${token}` },
            });

            setUser(updatedUser);
            setEditMode(false);
        } catch (err) {
            console.error("Error updating user data:", err);
            setError("Failed to update user data. Please try again.");
        }
    };

    const handleDeleteAccount = async () => {
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
        return <div>{error}</div>;
    }

    return (
        <div>
            <h1>Profile Page</h1>
            {user ? (
                <div>
                    <h2>User Details</h2>
                    {editMode ? (
                        <>
                            <p><strong>Username:</strong> <input type="text" name="username" value={updatedUser.username} onChange={handleInputChange} /></p>
                            <p><strong>Email:</strong> <input type="email" name="email" value={updatedUser.email} onChange={handleInputChange} /></p>
                            <p><strong>First Name:</strong> <input type="text" name="firstName" value={updatedUser.firstName} onChange={handleInputChange} /></p>
                            <p><strong>Last Name:</strong> <input type="text" name="lastName" value={updatedUser.lastName} onChange={handleInputChange} /></p>
                            <p><strong>Bio:</strong> <textarea name="bio" value={updatedUser.bio} onChange={handleInputChange}></textarea></p>
                            <button onClick={handleSaveChanges}>Save Changes</button>
                            <button onClick={handleEditToggle}>Cancel</button>
                        </>
                    ) : (
                        <>
                            <p><strong>Username:</strong> {user.username}</p>
                            <p><strong>Email:</strong> {user.email}</p>
                            <p><strong>Full Name:</strong> {user.firstName} {user.lastName}</p>
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
