import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar'; 
import Home from './Home';
import Login from './Login';
import Signup from './Signup';
import UserProfile from './UserProfile';
// import EditPage from './EditPage';
import ViewHistory from './ViewHistory';
// import PostPage from './PostPage';
import Page from './Page';
import SearchResults from './SearchResults';
import EditPage from './EditPage';

function App() {
  const [user, setUser] = useState(null);

  const handleUser = (user) => setUser(user);

  const handleLogout = () => {
    fetch('/logout', {
      method : "DELETE",
    }).then(() => {
      setUser(null);
    })
  }
  console.log(user)

  useEffect(()=>{
    fetch('/check_session').then((res) => {
      if (res.ok) {
        res.json().then((userObj) => setUser(userObj));
      }
    })

  }, [])

  return (
    <Router>
      <div className="App">
        <Navbar user={user} handleLogout={handleLogout}/> 
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/login" component={()=><Login handleUser={handleUser} />} />
          <Route path="/signup" component={()=><Signup handleUser={handleUser} />} />
          <Route path="/page/:pageId" component={Page} />
          <Route path="/history/:pageId" component={ViewHistory} />
          <Route path="/edit/:pageId" component={()=><EditPage user={user} />} />
          <Route path="/search/:query" component={SearchResults} />
          {user && <Route path="/profile" component={()=><UserProfile userId={user.id} />} />}
          {/* <Route path="/edit/:pageId" component={EditPage} />
          <Route path="/post" component={PostPage} /> */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
