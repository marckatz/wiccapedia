import React, { useEffect, useState } from "react";
import { useParams, Link, useHistory } from "react-router-dom";

function SearchResults(){
    const {query} = useParams()
    const [results, setResults] = useState([]) 
    const history = useHistory()
    
    useEffect(()=>{
        fetch(`/search_by_title/${query}`)
        .then(r=> r.ok? r.json(): [])
        .then(pages => {
            if(pages.length === 1){
                history.push(`/page/${pages[0].title}`)
            }
            setResults(pages)
        })
    },[query]);

    const result_list = results.map(page => {
        let underscoredTitle = page.title.replaceAll(' ', '_')
        return <Link to={`/page/${underscoredTitle}`} key={page.id}><h2>{page.title}</h2></Link>
    })

    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-start">
                <h1>Search Results for: "{query}":</h1>
            </div>
            <hr />
            {result_list}
        </div>
    )

}

export default SearchResults