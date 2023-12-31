import React, { useEffect, useState } from 'react';
import { useParams, Link, useHistory } from 'react-router-dom'

function Page() {
  const { pageId } = useParams();
  const [title, setTitle] = useState(' ')
  const [text, setText] = useState('')
  const [author, setAuthor] = useState('')
  const [lastEditor, setLastEditor] = useState('')
  const history = useHistory()

  useEffect(() => {
    fetch(`/pages/${pageId}`)
      .then(r => {
        if (r.ok) {
          return r.json()
        }
        else {
          history.push('/notfound')
        }
      })
      .then(page => {
        setTitle(page.title)
        setText(page.text)
        setAuthor(page.author)
        // console.log(page.edits)
        if (page.edits.length) {
          const length = page.edits.length
          setLastEditor(page['edits'][length - 1].user.username)
        }
      })
      .catch(error => {
      })
  }, [pageId])


  return (
    <div className="container mt-5">
      <div className="row row-cols-2 align-items-center">
        <div className="col-9">
          <h1 className="lh-base fw-bold" style={{ whiteSpace: 'pre-wrap' }}>
            {title}
          </h1>
        </div>
        <div className="col-3 d-flex justify-content-end">
          <Link to={`/edit/${pageId}`}>
            <button className="btn btn-outline-info btn-sm me-2" style={{ width: "100px" }}>Edit</button>
          </Link>
          <Link to={`/history/${pageId}`}>
            <button className="btn btn-outline-secondary btn-sm" style={{ width: "100px" }}>View History</button>
          </Link>
        </div>
      </div>
      <hr />
      <h5>By: {author}</h5>
      {lastEditor && <h6>Last edited by: {lastEditor}</h6>}
      <div className="mt-4" style={{ whiteSpace: "pre-wrap" }} dangerouslySetInnerHTML={{ __html: text }}></div>
    </div>
  );
}

export default Page;
