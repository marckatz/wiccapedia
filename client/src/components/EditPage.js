import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";

function EditPage({ user }) {
    const { pageId } = useParams()
    const [title, setTitle] = useState(' ')
    const [text, setText] = useState('')
    const [id, setId] = useState(0)
    const [originalText, setOriginalText] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/pages/${pageId}`)
            .then(r => r.json())
            .then(page => {
                setTitle(page.title)
                setText(page.text)
                setId(page.id)
                setOriginalText(page.text);
            })
    }, [])

    function handleSubmit(e) {
        e.preventDefault()
        if (text === originalText) {
            setError("No changes detected in the edit!");
            return;
        }
        const edit_json = {
            page_id: id,
            user_id: user.id,
            new_text: text
        }
        fetch('/create_edit', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(edit_json),
        })
            .then(r => {
                if (r.ok) {
                    window.location = `/page/${pageId}`
                }
            })
        // .then(r => r.json())
        // .then(edit => console.log(edit))
    }

    return (
        <div className="container mt-5">
            <div className="row row-cols-2 align-items-center">
                <div className="col-9">
                    <h1 className="lh-base" style={{whiteSpace:'pre-wrap'}}>
                        Editing <span className="fw-bold">{title} </span>
                    </h1>
                </div>
                <div className="col-3 d-flex justify-content-end">
                    <Link to={`/page/${pageId}`}>
                        <button className="btn btn-outline-info btn-sm me-2 text-truncate" style={{ width: "100px", whiteSpace: 'pre' }}>{title}</button>
                    </Link>
                    <Link to={`/history/${pageId}`}>
                        <button className="btn btn-outline-secondary btn-sm" style={{ width: "100px" }}>View History</button>
                    </Link>
                </div>
            </div>
            <hr />
            {user ? (
                <>
                    {error && <div className="alert alert-danger">{error}</div>}
                    <div onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <textarea
                                className="form-control"
                                value={text}
                                onChange={(e) => setText(e.target.value)}
                                style={{fontFamily:'monospace'}}
                                rows="25"
                            ></textarea>
                        </div>
                        <button className="btn btn-danger mb-5" onClick={handleSubmit}>
                            Submit Changes
                        </button>
                    </div>
                </>
            ) : (
                <h2>Please login or sign up to edit</h2>
            )
            }
        </div>
    );
}

export default EditPage;
