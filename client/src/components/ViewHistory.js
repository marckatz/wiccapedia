import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import EditCard from "./EditCard";

function ViewHistory() {
    const { pageId } = useParams()
    const [title, setTitle] = useState(' ')
    const [edits, setEdits] = useState([])

    useEffect(() => {
        fetch(`/pages/${pageId}`)
            .then(r => r.json())
            .then(page => {
                setTitle(page.title)
                setEdits(page.edits)
            })
    }, [])

    const editList = edits.map(edit => {
        return <EditCard key={edit.id} edit={edit} />
    })

    return (
        <div className="container mt-5">
            <div className="row row-cols-2 align-items-center">
                <div className="col-9">
                    <h1 className="text-truncate lh-base mb-0 fw-bold" style={{ whiteSpace: 'pre' }}>
                        {title}
                    </h1>
                </div>
                <div className="col-3">
                    <Link to={`/edit/${pageId}`}>
                        <button className="btn btn-outline-primary btn-sm me-2" style={{ width: "100px" }}>Edit</button>
                    </Link>
                    <Link to={`/page/${pageId}`}>
                        <button className="btn btn-outline-secondary btn-sm text-truncate" style={{ width: "100px", whiteSpace: 'pre' }}>{title}</button>
                    </Link>
                </div>
            </div>
            <hr />
            <div className="mx-5">
                {editList}
            </div>
        </div>
    )
}

export default ViewHistory