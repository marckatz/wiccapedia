import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import StatCard from './StatCard';

function Home() {
  const title = "Welcome to Wiccapedia"
  const text = "This is a platform for all things Wiccan."
  const [pages, setPages] = useState([])
  const [userStats, setUserStats] = useState([])
  const [pageStats, setPageStats] = useState([])

  useEffect(() => {
    fetch('/pages')
      .then(r => r.json())
      .then(p => setPages(p))

    fetch('/get_user_stats')
      .then(r => r.json())
      .then(u => setUserStats(u))

    fetch('/get_page_stats')
      .then(r => r.json())
      .then(p => setPageStats(p))


  }, [])

  const quickRender1 = userStats.map(user => <StatCard key = {user.id} name = {user.username} stat={user.num_of_edits}/>)
  const quickRender2 = pageStats.map(page => <StatCard key = {page.id} name = {page.title} stat= {page.num_of_edits}/>)
  return (
    <div className="home-container">
      <div className="container mt-5">
        <div className="d-flex justify-content-between align-items-start">
          <h1>{title}</h1>
          <div>
            <Link to={`/page/${Math.floor(Math.random() * pages.length) + 1}`}>
              <button className="btn btn-outline-primary btn-sm mr-2">Random Article</button>
            </Link>
          </div>
        </div>
        <hr />
        <p className="mt-4">{text}</p>
        <ul>
          {quickRender1}
        </ul>
        <ul>
          {quickRender2}
        </ul>
      </div>
    </div>
  );
}

export default Home;
