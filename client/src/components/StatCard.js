import React from "react";

function StatCard({ name, stat }) {
    return (
        <li className="list-group-item d-flex justify-content-between align-items-center">
            {name}
            <span className="badge bg-primary rounded-pill">{stat}</span>
        </li>
    )
}

export default StatCard