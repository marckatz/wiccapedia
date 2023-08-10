import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";

function EditPage({ user }) {
    const { pageId } = useParams()
    const [title, setTitle] = useState('')
    const [text, setText] = useState('')
    const [id, setId] = useState(null)

    useEffect(() => {
        fetch(`/pages/${pageId}`)
            .then(r => r.json())
            .then(page => {
                setTitle(page.title)
                setText(page.text)
                setId(page.id)
            })
    }, [])

    function handleSubmit(e) {
        e.preventDefault()
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
            <div className="d-flex justify-content-between align-items-start">
                <h1>Editing {title}</h1>
                <div>
                    <Link to={`/page/${pageId}`}>
                        <button className="btn btn-outline-primary btn-sm me-2">{title}</button>
                    </Link>
                    <Link to={`/history/${pageId}`}>
                        <button className="btn btn-outline-secondary btn-sm">History</button>
                    </Link>
                </div>
            </div>
            <hr />
            { user? (
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