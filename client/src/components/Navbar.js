import React, { useState } from 'react';
import Search from './Search';

function Navbar({username, handleLogout}) {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  // simple log out right now where handleUser is called to set user to '', if username exists in state, then logged in state shows
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white">
      <div className="collapse navbar-collapse d-flex justify-content-between" id="navbarNav">
        {/* Logo and Home link */}
        <div className="d-flex align-items-center">
          <a href="/">
            <img src="https://img.freepik.com/premium-vector/triple-moon-pentagram_257845-4104.jpg?w=1380"
              alt="Wiccapedia Logo" style={{ width: '40px', marginRight: '10px' }} />
          </a>
          <a className="navbar-brand" href="/">Wiccapedia</a>
        </div>

        {/* Search bar */}
        <Search />

        {/* Login/Logout */}
        <div>
          {username ? (
            <button className="btn btn-outline-danger ml-2" onClick={handleLogout}>Logout</button>
          ) : (
            <>
              <a className="btn btn-outline-danger ml-2" href="/login">Login</a>
              <a className="btn btn-outline-warning ml-2" href="/signup">Signup</a>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
