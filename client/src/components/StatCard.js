import React from "react";

function StatCard({ userStats, pageStats }) {
    const renderUserStats = userStats.map(user => <BuildUserColumns key={user.id} name={user.username} stat={user.num_of_edits} />)
    const renderPageStats = pageStats.map(page => <BuildPageColumns key={page.id} title={page.title} stat={page.num_of_edits} />)

    return (
        <>
            <h3 className='text-center'>Check Out Who's Editing What</h3>
            <div className='container d-flex flex-row justify-content-evenly'>
                <ul className='list-group w-25' >
                    <h5 className='text-center'>Top Editors</h5>
                    {renderUserStats}
                </ul>
                <ul className='list-group w-33' >
                    <h5 className='text-center'>Top Pages Edited</h5>
                    {renderPageStats}
                </ul>

            </div>
        </>
    )
}

function BuildUserColumns({name, stat}) {

    return (
        <li className="list-group-item d-flex justify-content-between align-items-center">
            <span className="fw-bold text-center" style={{width : '60%'}}>{name}</span>
            <span className="fw-bold"># of Edits: {stat}</span>
        </li>
    )
}

function BuildPageColumns({title, stat}) {

    return (
        <li className="list-group-item d-flex justify-content-between align-items-center">
            <span className="fw-bold text-center" style={{width : '75%'}}>{title}</span>
            <span className="fw-bold"># of Edits: {stat}</span>
        </li>
    )
}
export default StatCard


