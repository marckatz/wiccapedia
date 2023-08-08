import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar'; 
import Home from './Home';
import Login from './Login';
import Signup from './Signup';
// import UserProfile from './UserProfile';
// import EditPage from './EditPage';
// import ViewHistory from './ViewHistory';
// import PostPage from './PostPage';
import Page from './Page';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/signup" component={Signup} />
          <Route path="/page/:pageId" component={Page} />
          {/* <Route path="/profile" component={UserProfile} />
          <Route path="/edit/:pageId" component={EditPage} />
          <Route path="/history/:pageId" component={ViewHistory} />
          <Route path="/post" component={PostPage} /> */}
          
        </Switch>
      </div>
    </Router>
  );
}

export default App;
