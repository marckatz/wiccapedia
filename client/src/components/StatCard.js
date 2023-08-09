import React from "react";

function StatCard({ name, stat }) {
    return (
        <li className="list-group-item d-flex justify-content-around align-items-center">
            <span className="fw-bold">{name}</span>
            <span className="fw-bold">{stat}</span>
        </li>
    )
}

export default StatCard