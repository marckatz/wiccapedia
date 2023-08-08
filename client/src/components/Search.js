import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

function Search(props) {
  const [query, setQuery] = useState('');
  const history = useHistory()

  const handleSearch = (e) => {
    e.preventDefault()
    if(query){
      history.push(`/search/${query}`)
    }
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
        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </div>
    </form>
  );
}

export default Search;
