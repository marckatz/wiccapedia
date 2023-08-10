import React from "react";

function EditCard({edit}){
    const username = edit.user.username
    const diff = edit.diff

    function readableDiff(diff_string){
        let diff_list = diff_string.split('\n')
        let line_nums = diff_list.splice(0,3)[2].match(/[-+]\d,\d/g)
        let left = []
        let right = []
        let imbalance = 0
        diff_list.forEach(line => {
            if(line[0] === '-'){
                left.push(line)
                imbalance--
            }
            else if(line[0] === '+'){
                right.push(line)
                imbalance++
            }
            else{
                if(imbalance !== 0){
                    (imbalance > 0?left:right).push(...Array(Math.abs(imbalance)).fill(' '))
                    imbalance = 0
                }
                left.push(line)
                right.push(line)
            }
        });
        // return [left.join('\n'), right.join('\n')]
        const rows = left.map((leftLine, index) => {
            let rightLine = right[index]
            return intoColumns(leftLine, rightLine, index)
        })
        return rows
    }

    function intoColumns(left, right, index){
        let color = ""
        if(index !== 0){
            if(left[0] === '-' && right[0] == '+'){
                color = "bg-info bg-opacity-50"
            }
            else if(left[0] === '-'){
                color = "bg-danger bg-opacity-50"
            }
            else if(right[0] === '+'){
                color = "bg-success bg-opacity-50"
            }
        }
        return (
            <div className="row font-monospace border border-secondary rounded align-items-stretch mx-5" style={{height:'1.5rem', overflow:'hidden'}} key={index}>
                <div className={`col ${color} h-100 border-end border-secondary object-fit-fill`}>{left}</div>
                <div className={`col ${color} h-100 object-fit-fill`}>{right}</div>
            </div>
        )
    }

    return (
        <div className="container mb-5" style={{overflow:"auto"}}>
            <h3>Edited by {username}</h3>
            {/* <p style={{whiteSpace:'pre-wrap'}}>{diff}</p> */}
            {/* <p className="font-monospace" style={{whiteSpace:'pre-wrap', float:'left'}}>{readableDiff(diff)[0]}</p>
            <p className="font-monospace" style={{whiteSpace:'pre-wrap', float:'right'}}>{readableDiff(diff)[1]}</p> */}
            {readableDiff(diff)}
        </div>
    )
}
{/* <span style={{textAlign:'left'}}></span> */}
{/* <span style={{float:'right'}}></span> */}

export default EditCard