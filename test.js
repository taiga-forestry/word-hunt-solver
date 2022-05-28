/**
 * Resets all the letter-boxes to nothing
 */
const clearBoard = () => {
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            let id = String(i) + String(j);
            document.getElementById(id).value = " ";
        }
    }
}

/**
 * 
 */
const solveBoard = () => {
    let board = "";

    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            let id = String(i) + String(j);
            board += document.getElementById(id).value;
        }
    }
}