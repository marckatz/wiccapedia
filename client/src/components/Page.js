import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom'

function Page() {
  const { pageId } = useParams();
  const [title, setTitle] = useState(' ')
  const [text, setText] = useState('')
  const [author, setAuthor] = useState('')
  const [lastEditor, setLastEditor] = useState('')

  useEffect(() => {
    fetch(`/pages/${pageId}`)
      .then(r => r.json())
      .then(page => {
        setTitle(page.title)
        setText(page.text)
        setAuthor(page.author)
      })
  }, [])


  return (
    <div className="container mt-5">
      <div className="row row-cols-2 align-items-center">
          <div className="col-9">
            <h1 className="text-truncate lh-base mb-0 fw-bold" style={{whiteSpace:'pre'}}>
              {title}
            </h1>
          </div>
          <div className="col-3">
              <Link to={`/edit/${pageId}`}>
                  <button className="btn btn-outline-primary btn-sm me-2" style={{width:"100px"}}>Edit</button>
              </Link>
              <Link to={`/history/${pageId}`}>
                  <button className="btn btn-outline-secondary btn-sm" style={{width:"100px"}}>View History</button>
              </Link>
          </div>
      </div>
      <hr />
      <h4>By: {author}</h4>
      <div className="mt-4" style={{ whiteSpace: "pre-wrap" }} dangerouslySetInnerHTML={{ __html: text }}></div>
    </div>
  );
}

export default Page;
