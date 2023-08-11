import React from "react";

function StatCard({ userStats, pageStats }) {
    const renderUserStats = userStats.map(user => <BuildUserColumns key={user.id} name={user.username} stat={user.num_of_edits} />)
    const renderPageStats = pageStats.map(page => <BuildPageColumns key={page.id} title={page.title} stat={page.num_of_edits} />)

    return (
        <>
            <h3 className='text-center'>Check Out Who's Editing What</h3>
            <div className='container row justify-content-evenly mb-5'>
                <div className='border border-secondary col-4'>
                    <div className="row"><h5 className='col text-center'>Top Editors</h5></div>
                    {renderUserStats}
                </div>
                <div className='border border-secondary col-4' >
                    <h5 className='text-center'>Top Pages Edited</h5>
                    {renderPageStats}
                </div>

            </div>
        </>
    )
}

function BuildUserColumns({name, stat}) {

    return (
        <div className="row justify-content-between align-items-between border-top border-secondary">
            <div className="col fw-bold text-center" >{name}</div>
            <div className="col fw-bold text-center"># of Edits: {stat}</div>
        </div>
    )
}

function BuildPageColumns({title, stat}) {

    return (
        <div className="row justify-content-between align-items-between border-top border-secondary">
            <div className="col fw-bold text-center" >{title}</div>
            <div className="col fw-bold text-center"># of Edits: {stat}</div>
        </div>
    )
}
export default StatCard


