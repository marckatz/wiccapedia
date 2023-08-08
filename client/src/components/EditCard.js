import React from "react";

function EditCard({edit}){
    const username = edit.user.username
    const diff = edit.diff

    return (
        <div>
            <h3>Edited by {username}</h3>
            <p style={{whiteSpace:'pre-wrap'}}>{diff}</p>
        </div>
    )
}

export default EditCard