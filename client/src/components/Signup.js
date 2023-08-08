import React, { useState } from 'react';

function Signup() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({ username: '', password: '' });

  const handleSignup = () => {
    let isValid = true;

    // Reset errors
    setErrors({ username: '', password: '' });

    // Validate username and password length
    if (username.length < 6) {
      setErrors((prevErrors) => ({ ...prevErrors, username: 'username too short!' }));
      isValid = false;
    }

    if (password.length < 6) {
      setErrors((prevErrors) => ({ ...prevErrors, password: 'password too short!' }));
      isValid = false;
    }

    // Check if username exists
    // if () {
    // setErrors((prevErrors) => ({ ...prevErrors, username: 'username already exists!' }));
    // isValid = false
    // }

    if (isValid) {
      // bulabula
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h2 className="text-center">Signup</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <div className="form-group">
              <label>Username:</label>
              <input
                type="text"
                className={`form-control ${errors.username && 'is-invalid'}`}
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
              {errors.username && <div className="invalid-feedback">{errors.username}</div>}
            </div>
            <div className="form-group">
              <label>Password:</label>
              <input
                type="password"
                className={`form-control ${errors.password && 'is-invalid'}`}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              {errors.password && <div className="invalid-feedback">{errors.password}</div>}
            </div>
            <div className="text-center">
              <button className="btn btn-warning" onClick={handleSignup}>
                Signup
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Signup;
