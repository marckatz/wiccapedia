import { Link } from 'react-router-dom';
import Search from './Search';

function Navbar({ user, handleLogout }) { 
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white">
      <div className="collapse navbar-collapse d-flex justify-content-between" id="navbarNav">
        {/* Logo and Home link */}
        <div className="d-flex align-items-center">
          <Link to="/">
            <img src="https://img.freepik.com/premium-vector/triple-moon-pentagram_257845-4104.jpg?w=1380"
              alt="Wiccapedia Logo" style={{ width: '40px', marginRight: '10px' }} />
          </Link>
          <Link className="navbar-brand" to="/">Wiccapedia</Link>
        </div>

        {/* Search bar */}
        <Search />

        {/* Login/Logout */}
        <div>
          {user ? (
            <>
              <a className="btn btn-outline-success me-2" href="/post">PostPage</a>
              <a className="btn btn-outline-info me-2" href="/profile">Profile</a>
              <button className="btn btn-outline-danger me-2" onClick={handleLogout}>Logout</button>
            </>
          ) : (
            <>
              <a className="btn btn-outline-danger me-2" href="/login">Login</a>
              <a className="btn btn-outline-warning me-2" href="/signup">Signup</a>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
