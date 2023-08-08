import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";

function EditPage({ userId }) {
    const { pageId } = useParams()
    const [title, setTitle] = useState('')
    const [text, setText] = useState('')

    useEffect(() => {
        fetch(`/pages/${pageId}`)
            .then(r => r.json())
            .then(page => {
                setTitle(page.title)
                setText(page.text)
            })
    }, [])

    function handleSubmit(e) {
        e.preventDefault()
        const edit_json = {
            page_id: pageId,
            user_id: userId,
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
            <div className="d-flex justify-content-between align-items-start">
                <h1>Editing {title}</h1>
                <div>
                    <Link to={`/page/${pageId}`}>
                        <button className="btn btn-outline-primary btn-sm mr-2">{title}</button>
                    </Link>
                    <Link to={`/history/${pageId}`}>
                        <button className="btn btn-outline-secondary btn-sm">History</button>
                    </Link>
                </div>
            </div>
            <hr />
            { userId? (
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <textarea value={text} onChange={(e) => setText(e.target.value)}></textarea>
                </div>
                <button className="btn btn-danger" onClick={handleSubmit}>
                    Submit Changes
                </button>
            </form>
            ) : (
                <h2>Please login or sign up to edit</h2>
            )
            }
        </div>
    )
}

export default EditPage