import React from 'react';
import authService from '../services/authService';

const Dashboard = () => {
  const user = JSON.parse(localStorage.getItem('user'));

  const handleLogout = () => {
    authService.logout();
    window.location.reload();
  };

  if (!user) {
    return <h2>Please log in</h2>;
  }

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Welcome, {user.user.username}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;
