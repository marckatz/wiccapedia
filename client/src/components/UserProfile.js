import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; 

function UserProfile({ user }) {
  // const [userData, setUserData] = useState({});
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [showChangePasswordForm, setShowChangePasswordForm] = useState(false);
  const [userEdits, setUserEdits] = useState([]);
  const [userPosts, setUserPosts] = useState([]);

  useEffect(() => {
    // Fetch user's edits
    // fetch(`/users/${user.id}/edits`)
    //   .then((response) => response.json())
    //   .then((data) => setUserEdits(data))
    //   .catch((error) => console.error("Error fetching user edits:", error));

    // Fetch user's posts
    fetch(`/users/${user.id}/posts`)
      .then((response) => response.json())
      .then((data) => setUserPosts(data))
      .catch((error) => console.error("Error fetching user edits:", error));
    }, []);

  const handlePasswordChange = async () => {
    setSuccess('');
    setError('');

    if (newPassword !== confirmPassword) {
      setError("New password and confirm password do not match.");
      return;
    }

    try {
      const response = await fetch('/change_password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          userId: user.id,
          currentPassword: currentPassword,
          newPassword: newPassword,
        }),
      });

      const data = await response.json();

      if (response.status !== 200) {
        setError(data.error || "Failed to change password.");
      } else {
        console.log("Password changed successfully!");
        setSuccess("Password changed successfully!");
        setCurrentPassword('');
        setNewPassword('');
        setConfirmPassword('');
      }
    } catch (error) {
      setError("Error changing password.");
    }
  };

  const handleCancelChange = () => {
    setCurrentPassword('');
    setNewPassword('');
    setConfirmPassword('');
    setSuccess('');
    setError('');
    setShowChangePasswordForm(false);
  };

  return (
    <div className="container mt-5">
      <h1>My Profile</h1>
      <hr />
      <h3>Username: {user.username}</h3>

      {/* Change Password Section */}
      <div className="mt-5">
        <h4>Change Password</h4>
        {error && <div className="alert alert-danger">{error}</div>}
        {success && <div className="alert alert-success">{success}</div>}

        {showChangePasswordForm ? (
          <form onSubmit={e=>e.preventDefault()}>
            <div className="mb-1">
              <label className='form-label'>Current Password:</label>
              <input
                type="password"
                className="form-control"
                value={currentPassword}
                onChange={(e) => setCurrentPassword(e.target.value)}
              />
            </div>
            <div className="mb-1">
              <label className='form-label'>New Password:</label>
              <input
                type="password"
                className="form-control"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
              />
            </div>
            <div className="mb-3">
              <label className='form-label'>Confirm New Password:</label>
              <input
                type="password"
                className="form-control"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
            </div>
            <div className='mb-1'>
              <button 
                className="btn btn-danger" 
                onClick={handlePasswordChange}
                disabled={!currentPassword || !newPassword || !confirmPassword}
              >
                Change Password
              </button>
              <button 
                className="btn btn-secondary ms-3" 
                onClick={handleCancelChange} 
              >
                Cancel Change
              </button>
            </div>
          </form>
        ) : (
          <button 
            className="btn btn-outline-danger" 
            onClick={() => setShowChangePasswordForm(true)}
          >
            Change Password
          </button>
        )}
      </div>

      {/* user's edits */}
      <div className="mt-5">
        <h4>My Edits</h4>
        <ul>
          {user.edits.filter((value, index, self) => 
            self.findIndex(v => v.page.title === value.page.title) === index
          ).map((edit, index) => (
            <li key={index}>
              <Link to={`/page/${edit.page.title}`} className="link-info">
                {edit.page.title}
              </Link>
            </li>
          ))}
        </ul>
      </div>

      {/* user's posts */}
      <div className="mt-5">
        <h4>My Posts</h4>
        <ul>
          {userPosts.map((post, index) => {
            return (
              <li key={index}>
                <Link to={`/page/${post.title}`} className="link-info">
                  {post.title}
                </Link>
              </li>
            );
          })}
        </ul>
      </div>

    </div>
  );
}

export default UserProfile;
