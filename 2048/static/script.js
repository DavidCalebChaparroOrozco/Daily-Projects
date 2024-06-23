let board = [];

document.addEventListener('DOMContentLoaded', (event) => {
    startGame();
    document.addEventListener('keydown', handleKeyPress);
    document.getElementById('autoplay').addEventListener('click', autoplayGame);
    document.getElementById('restart').addEventListener('click', startGame);
});

function startGame() {
    fetch('/start', {
        method: 'POST',
    }).then(response => response.json())
        .then(data => {
            board = data.board;
            renderBoard();
        });
}

function handleKeyPress(event) {
    let direction;
    if (event.key === 'ArrowLeft') direction = 'left';
    if (event.key === 'ArrowRight') direction = 'right';
    if (event.key === 'ArrowUp') direction = 'up';
    if (event.key === 'ArrowDown') direction = 'down';
    if (direction) move(direction);
}

function move(direction) {
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ direction: direction, board: board })
    }).then(response => response.json())
        .then(data => {
            board = data.board;
            if (data.game_over) {
                alert('Game Over! Click Restart to play again.');
            }
            renderBoard();
        });
}

function autoplayGame() {
    fetch('/autoplay', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ board: board })
    }).then(response => response.json())
        .then(data => {
            board = data.board;
            renderBoard();
        });
}

function renderBoard() {
    const boardDiv = document.getElementById('board');
    boardDiv.innerHTML = '';
    board.forEach(row => {
        row.forEach(cell => {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell';
            cellDiv.textContent = cell === 0 ? '' : cell;
            boardDiv.appendChild(cellDiv);
        });
    });
}
