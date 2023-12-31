import React from "react";

function EditCard({edit}){
    const username = edit.user.username
    const diff = edit.diff

    function readableDiff(diff_string){
        let diff_list = diff_string.split('\n')
        diff_list.splice(0,3)
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
                // left.push(line)
                // right.push(line)
            }
        });
        if(imbalance !== 0){
            (imbalance > 0?left:right).push(...Array(Math.abs(imbalance)).fill(' '))
            imbalance = 0
        }
        // return [left.join('\n'), right.join('\n')]
        const rows = left.map((leftLine, index) => {
            let rightLine = right[index]
            return intoColumns(leftLine, rightLine, index)
        })
        return rows
    }

    function intoColumns(left, right, index){
        let color_left = ""
        let color_right = ""
        // if(index !== 0){
            if(left[0] === '-' && right[0] === '+'){
                color_left = "bg-info bg-opacity-50"
                color_right = "bg-info bg-opacity-50"
            }
            else if(left[0] === '-'){
                color_left = "bg-danger bg-opacity-50"
            }
            else if(right[0] === '+'){
                color_right = "bg-success bg-opacity-50"
            }
        // }
        return (
            <div className="row font-monospace border border-secondary rounded align-items-stretch mx-5"key={index}style={{minHeight:'1.5rem'}} >
                <div className={`col ${color_left} border-end border-secondary text-break`} >{left}</div>
                <div className={`col ${color_right} border-start border-secondary text-break`}>{right}</div>
            </div>
        )
    }

    return (
        <div className="container mb-5" style={{overflow:"auto"}}>
            <h3>Edited by {username} on {edit.time}</h3>
            {readableDiff(diff)}
        </div>
    )
}


export default EditCard