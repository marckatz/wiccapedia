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
          <Link to={`/edit/${pageId}`}>
            <button className="btn btn-outline-primary btn-sm me-2">Edit</button>
          </Link>
          <Link to={`/history/${pageId}`}>
            <button className="btn btn-outline-secondary btn-sm">View History</button>
          </Link>
        </div>
      </div>
      <hr />
      <div className="mt-4" style={{whiteSpace:"pre-wrap"}} dangerouslySetInnerHTML={{__html:text}}></div>
    </div>
  );
}

export default Page;
