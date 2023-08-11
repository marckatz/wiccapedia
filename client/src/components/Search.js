import React, { useState } from 'react';
// import { Link } from 'react-router-dom';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';

function Search(props) {
  const [query, setQuery] = useState('');
  const history = useHistory()

  const handleSearch = (e) => {
    e.preventDefault()
    if(query){
      fetch(`/search_by_title/${query}`)
      .then(r=> r.ok? r.json(): [])
      .then(pages => {
          if(pages.length === 1){
              let underscoredTitle = pages[0].title.replaceAll(' ', '_')
              history.push(`/page/${underscoredTitle}`)
          }
          else{
            history.push(`/search/${query}`, {params : pages})
          }

      })
    }
  }

  return (
    <form className="row row-cols-lg-auto align-items-center g-2" onSubmit={handleSearch}>
      <div className='col'>
        <input
          className="form-control me-sm-2"
          type="search"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Search"
          aria-label="Search"
        />
      </div>
      <div className='col'>
        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </div>
    </form>
  );
}

export default Search;
