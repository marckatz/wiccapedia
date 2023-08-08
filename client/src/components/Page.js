import React from 'react';

function Page({ title, text }) {
  return (
    <div className="container mt-5">
      <div className="d-flex justify-content-between align-items-start">
        <h1>{title}</h1>
        <div>
          <button className="btn btn-outline-primary btn-sm mr-2">Edit</button>
          <button className="btn btn-outline-secondary btn-sm">View History</button>
        </div>
      </div>
      <hr />
      <p className="mt-4">{text}</p>
    </div>
  );
}

export default Page;
