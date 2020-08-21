const canvas = document.getElementById('canvas')
const queenImage = document.getElementById("queenImage")
const nextSol = document.getElementById('nextSol')
const prevSol = document.getElementById('prevSol')
const boardNumber = document.getElementById('board-number')
const ctx = canvas.getContext('2d')
const white = 'rgb(200, 200, 200)'
const board_dimension = Queens[0].length
const cell_size = 70
var count = -1

canvas.width = board_dimension * cell_size
canvas.height = board_dimension * cell_size


const display_board = () => {
    let down_by = 0

    for (let row = 0; row < board_dimension; row++) {
        down_by = row * cell_size

        for (let col = 0; col < board_dimension; col++) {

            if ( row % 2  === 0 && col % 2 !== 0 ) {
                
                ctx.fillStyle = white
                ctx.fillRect(
                    (col - 1) * cell_size,
                    row + down_by,
                    cell_size,
                    cell_size
                )

            }
            
            if ( row % 2 !== 0 && col % 2 !== 0 ){
                // row % 2 !== 0
                ctx.fillStyle = white
                ctx.fillRect(
                    col * cell_size,
                    row + down_by,
                    cell_size,
                    cell_size
                )
            }

        }
    }
}

const placeQueens = (board) => {
    for (let row = 0; row < board_dimension; row++) {
        down_by = row * cell_size

        for (let col = 0; col < board_dimension; col++) {

            if ( board[row][col] === "Q" ) {
                ctx.drawImage(
                    queenImage,
                    col * cell_size + ( ( cell_size - queenImage.width ) / 2),
                    row + down_by + ( ( cell_size - queenImage.height ) / 2)
                )
            }

        }
    }
}


const nextBoard = (pn) => {
    
    if (pn == 'add')
        count += 1

    else 
        count -= 1

    if ( count < Queens.length && count >= 0 ) {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        display_board()
        placeQueens(Queens[count])
        boardNumber.innerText = `${count + 1} / ${Queens.length}`
    }

}

nextSol.addEventListener('click', () => nextBoard('add'))
prevSol.addEventListener('click', () => nextBoard('sub'))

nextBoard('add')