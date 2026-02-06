const board = document.getElementById('board');
const statusEl = document.getElementById('status');
const resetBtn = document.getElementById('resetBtn');
const popup = document.getElementById('gameOverPopup');
const closePopupBtn = document.getElementById('closePopup');
const boardSizeSelect = document.getElementById('boardSize');
const finalScoreEl = document.getElementById('finalScore');

let size = parseInt(boardSizeSelect.value);
let knightPos = null;
let moveCount = 0;

const knightMoves = [
  [2, 1], [1, 2], [-1, 2], [-2, 1],
  [-2, -1], [-1, -2], [1, -2], [2, -1]
];

function isValidMove(x, y) {
  return x >= 0 && x < size && y >= 0 && y < size;
}

function getCell(x, y) {
  return document.querySelector(`.cell[data-x='${x}'][data-y='${y}']`);
}

function resetBoard() {
  size = parseInt(boardSizeSelect.value); 
  board.innerHTML = '';
  board.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
  board.style.gridTemplateRows = `repeat(${size}, 1fr)`;


  knightPos = null;
  moveCount = 0;
  statusEl.textContent = "Click a square to place the knight.";
  popup.style.display = "none"; 

  for (let y = 0; y < size; y++) {
    for (let x = 0; x < size; x++) {
      const cell = document.createElement('div');
      cell.classList.add('cell', (x + y) % 2 === 0 ? 'white' : 'black');
      cell.dataset.x = x;
      cell.dataset.y = y;
      cell.addEventListener('click', () => handleCellClick(x, y));
      board.appendChild(cell);
    }
  }
}

function handleCellClick(x, y) {
  const cell = getCell(x, y);
  if (cell.textContent) return;

  if (!knightPos) {
    knightPos = [x, y];
    moveCount = 1;
    cell.classList.add('knight');
    cell.textContent = moveCount;
    statusEl.textContent = "Knight placed! Make your moves.";
  } else {
    const dx = x - knightPos[0];
    const dy = y - knightPos[1];

    if (knightMoves.some(([mx, my]) => mx === dx && my === dy)) {
      const [kx, ky] = knightPos;
      const prevCell = getCell(kx, ky);
      prevCell.classList.remove('knight');

      knightPos = [x, y];
      moveCount++;
      cell.classList.add('knight');
      cell.textContent = moveCount;

      if (moveCount === size * size) {
        showPopup(true);
        return;
      }

      if (!hasValidMoves(knightPos[0], knightPos[1])) {
        showPopup(false);
      }
    }
  }
}

function hasValidMoves(x, y) {
  return knightMoves.some(([dx, dy]) => {
    const nx = x + dx;
    const ny = y + dy;
    if (isValidMove(nx, ny)) {
      const nextCell = getCell(nx, ny);
      return !nextCell.textContent; 
    }
    return false;
  });
}

function showPopup(won) {
  finalScoreEl.textContent = won 
    ? `🎉 You Won! You visited all ${size * size} tiles!` 
    : `Game Over! Final Score: ${moveCount} moves`;
  popup.style.display = "flex";
}

resetBtn.addEventListener('click', resetBoard);
closePopupBtn.addEventListener('click', () => popup.style.display = "none");
boardSizeSelect.addEventListener('change', resetBoard);
resetBoard();
