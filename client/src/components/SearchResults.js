import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

function SearchResults(){
    const {query} = useParams()
    const [results, setResults] = useState([]) 

    useEffect(()=>{
        fetch(`/search_by_title/${query}`)
        .then(r=>r.json())
        .then(pages => {
            // if(pages.length === 1){jump to page}
            setResults(pages)
        })
    },[]);

    const result_list = results.map(page => {
        return <Link to={`/page/${page.id}`} key={page.id}><h2>{page.title}</h2></Link>
    })

    return (
        <div>
            {result_list}
        </div>
    )

}

export default SearchResults