import React from "react";

function StatCard({ userStats, pageStats }) {
    const renderUserStats = userStats.map(user => <BuildColumns key={user.id} name={user.username} stat={user.num_of_edits} />)
    const renderPageStats = pageStats.map(page => <BuildColumns key={page.id} name={page.title} stat={page.num_of_edits} />)

    return (
        <>
            <h3 className='text-center'>Check Out Who's Editing What</h3>
            <div className='container d-flex flex-row justify-content-evenly'>
                <ul className='list-group w-25' >
                    <h5 className='text-center'>Top Editors</h5>
                    {renderUserStats}
                </ul>
                <ul className='list-group w-25' >
                    <h5 className='text-center'>Top Pages Edited</h5>
                    {renderPageStats}
                </ul>

            </div>
        </>
    )
}

function BuildColumns({name, stat}) {

    return (
        <li className="list-group-item d-flex justify-content-around align-items-center">
            <span className="fw-bold">{name}</span>
            <span className="fw-bold"># of Edits: {stat}</span>
        </li>
    )
}

export default StatCard


