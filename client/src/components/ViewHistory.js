import React, {useState, useEffect} from "react";
import { useParams } from "react-router-dom";
import EditCard from "./EditCard";

function ViewHistory() {
    const { pageId } = useParams()
    const [title, setTitle] = useState('')
    const [edits, setEdits] = useState([])

    useEffect(() => {
        fetch(`http://localhost:5555/pages/${pageId}`)
            .then(r => r.json())
            .then(page => {
                setTitle(page.title)
                setEdits(page.edits)
            })
    },[])

    const editList = edits.map(edit =>{
        return <EditCard key={edit.id} edit={edit} /> 
    })

    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between align-items-start">
                <h1>{title}</h1>
            </div>
            <hr />
            <div>
                {editList}
            </div>
        </div>
    )
}

export default ViewHistory