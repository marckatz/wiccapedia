import React, { useState, useEffect } from "react";
import { useParams, Link, useHistory } from "react-router-dom";
import EditCard from "./EditCard";

function ViewHistory() {
    const { pageId } = useParams()
    const [title, setTitle] = useState(' ')
    const [edits, setEdits] = useState([])
    const history = useHistory()

    useEffect(() => {
        fetch(`/pages/${pageId}`)
            .then(r => {
                if (r.ok) {
                    return r.json()
                }
                else {
                    history.push('/notfound')
                }
            })
            .then(page => {
                setTitle(page.title)
                setEdits(page.edits)
            })
            .catch(e => history.push('/notfound'))
    }, [])

    const editList = edits.map(edit => {
        return <EditCard key={edit.id} edit={edit} />
    })

    return (
        <div className="container mt-5">
            <div className="row row-cols-2 align-items-center">
                <div className="col-9">
                    <h1 className="lh-base fw-bold" style={{ whiteSpace: 'pre-wrap' }}>
                        {title}
                    </h1>
                </div>
                <div className="col-3 d-flex justify-content-end">
                    <Link to={`/edit/${pageId}`}>
                        <button className="btn btn-outline-info btn-sm me-2" style={{ width: "100px" }}>Edit</button>
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