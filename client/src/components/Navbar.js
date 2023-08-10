import { Link, useHistory } from 'react-router-dom';
import Search from './Search';

function Navbar({ user, handleUser }) {
  const history = useHistory()
  const handleLogout = () => {
    fetch('/logout', {
      method : "DELETE",
    }).then(() => {
      handleUser(null);
      history.push('/')
    })
  }

  function handleLogin(){
    history.push('/login', {from:history.location.pathname})
  }
  function handleSignup(){
    history.push('/signup', {from:history.location.pathname})
  }
  
  return (
    <nav className="navbar navbar-expand-lg navbar-light justify-content-center">
      <div className="collapse navbar-collapse d-flex justify-content-between" id="navbarNav">
        {/* Logo and Home link */}
        <div className="d-flex align-items-center ms-2">
          <Link to="/">
            <img src="https://img.freepik.com/premium-vector/triple-moon-pentagram_257845-4104.jpg?w=1380"
              alt="Wiccapedia Logo" style={{ width: '40px', marginRight: '10px' }} className='rounded-4'/>
          </Link>
          <Link className="navbar-brand" to="/">Wiccapedia</Link>
        </div>

        {/* Search bar */}
        <Search />

        {/* Login/Logout */}
        <div>
          {user ? (
            <>
              <Link className="btn btn-outline-success me-2" to="/post">New Article</Link>
              <Link className="btn btn-outline-info me-2" to="/profile">Profile</Link>
              <button className="btn btn-outline-danger me-2" onClick={handleLogout}>Log Out</button>
            </>
          ) : (
            <>
              <div className="btn btn-outline-warning me-2" onClick={handleSignup}>Sign Up</div>
              <div className="btn btn-outline-danger me-2" onClick={handleLogin}>Log In</div>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
