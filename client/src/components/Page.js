import React, { useEffect, useState } from 'react';
import {useParams, Link} from 'react-router-dom'

function Page() {
  const {pageId} = useParams();
  const [title, setTitle] = useState('')
  const [text, setText] = useState('')

  useEffect(() => {
    fetch(`/pages/${pageId}`)
    .then(r=>r.json())
    .then(page => {
      setTitle(page.title)
      setText(page.text)
    })
  },[])


  return (
    <div className="container mt-5">
      <div className="d-flex justify-content-between align-items-start">
        <h1>{title}</h1>
        <div>
          <button className="btn btn-outline-primary btn-sm mr-2">Edit</button>
          <Link to={`/history/${pageId}`}>
            <button className="btn btn-outline-secondary btn-sm">View History</button>
          </Link>
        </div>
      </div>
      <hr />
      <p className="mt-4" style={{whiteSpace:"pre-wrap"}}>{text}</p>
    </div>
  );
}

export default Page;
