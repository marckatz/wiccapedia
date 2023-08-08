import React, { useState } from 'react';

function Search(props) {
  const [query, setQuery] = useState('');

  const handleSearch = (event) => {
    event.preventDefault();
    // bulabula
  };

  return (
    <form className="form-inline my-2 my-lg-0" onSubmit={handleSearch}>
      <input 
        className="form-control mr-sm-2" 
        type="search" 
        value={query} 
        onChange={e => setQuery(e.target.value)} 
        placeholder="Search" 
        aria-label="Search" 
      />
      <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  );
}

export default Search;
