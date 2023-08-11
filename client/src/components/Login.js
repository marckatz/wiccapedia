import React, { useState } from 'react';
import {useHistory} from 'react-router-dom';

function Login({handleUser}) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const [error, setError] = useState(''); 
  const history = useHistory()

  const handleLogin = async () => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username, password: password }),
      });

      const data = await response.json();

      if (response.status === 200) {
        console.log("Successfully logged in!", data);
        const prev = history.location.state && history.location.state.from
        if(prev && (prev !== '/login' && prev !== '/signup')){
          history.push(prev)
        }
        else{
          history.push('/')
        }
        handleUser(data)

      } else if (response.status === 401) {
        setError("Incorrect password. Please try again.");
      } else if (response.status === 404) {
        setError("User not found. Please try again.");
      } else {
        setError(data.error || "Failed to login. Please try again.");
      }

    } catch (error) {
      console.error("There was an error logging in", error);
      setError("An unexpected error occurred. Please try again later.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h2 className="text-center">Log In</h2>
          {error && <div className="alert alert-danger">{error}</div>}
          <form onSubmit={(e) => e.preventDefault()}>
            <div className="mb-1">
              <label className='form-label'>Username:</label>
              <input
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <p></p>
            <div className="mb-1">
              <label className='form-label'>Password:</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <p></p>
            <div className="text-center">
              <button className="btn btn-danger" onClick={handleLogin}>
                Log In
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
export default Login;
