import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Search(props) {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    e.preventDefault()
  }

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
      <Link to={`/search/${query}`}>
        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </Link>
    </form>
  );
}

export default Search;
