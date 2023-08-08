import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Search(props) {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    e.preventDefault()
  }

  return (
    <form className="row row-cols-lg-auto g-3 align-items-center" onSubmit={handleSearch}>
      <div className='col-12'>
        <input
          className="form-control me-sm-2"
          type="search"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Search"
          aria-label="Search"
        />
      </div>
      <div className='col-12'>
        <Link to={`/search/${query}`}>
          <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </Link>
      </div>
    </form>
  );
}

export default Search;
