import React, { useState, useEffect } from 'react';

const PostPage = ({ username }) => {
  const [pages, setPages] = useState([]);
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    fetch('/pages')
      .then(response => response.json())
      .then(data => {
        setPages(data);
      })
      .catch(error => {
        console.error("Error fetching the pages:", error);
      });
  }, []);

  const handlePostPage = () => {
    fetch('/pages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username: username, title: title, text: text, })
    })
      .then(response => response.json())
      .then(data => {
        setPages([...pages, data]);
        setTitle('');
        setText('');
        setIsSubmitted(true);
      })
      .catch(error => {
        console.error("Error posting the page:", error);
      });
  };

  return (
    <div className="container mt-5">
      <h1>Create New Page</h1>
      <hr />
      {isSubmitted && (
        <div className="alert alert-success" role="alert">
          Page submitted successfully!
        </div>
      )}
      <form>
        <div className="mb-3">
          <label htmlFor="pageTitle" className="form-label">Title</label>
          <input
            type="text"
            className="form-control"
            id="pageTitle"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter page title" />
        </div>

        <div className="mb-3">
          <label htmlFor="pageText" className="form-label">Text</label>
          <textarea
            className="form-control"
            id="pageText"
            rows="3"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter page content"></textarea>
        </div>

        <button type="button" className="btn btn-primary" onClick={handlePostPage}>
          Submit
        </button>
      </form>
    </div>
  );
}

export default PostPage;
