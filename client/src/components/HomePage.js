import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function HomePage({ title, text }) {  
  const [pages, setPages] = useState([]) 

  useEffect(() => {
    fetch('/pages')
    .then(r=>r.json())
    .then(p => setPages(p))
  },[])

  return (
    <div className="container mt-5">
      <div className="d-flex justify-content-between align-items-start">
        <h1>{title}</h1>
        <div>
          <Link to={`/page/${Math.floor(Math.random() * pages.length) + 1}`}>
            <button className="btn btn-outline-primary btn-sm me-2">Random Article</button>
          </Link>
        </div>
      </div>
      <hr />
      <p className="mt-4">{text}</p>
    </div>
  );
}

export default HomePage;
