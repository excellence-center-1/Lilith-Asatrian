const displayMatrix = (matrix) => matrix.map(row => row.join("  ")).join("\n");
const checkRows = (matrix, player) => matrix.some(row => row.every(cell => cell === player));
const checkColumns = (matrix, player) => {
  for(let i = 0; i<matrix.length; ++i) {
    return matrix.every(row => row[i] === player);
  }
  return false;
};  

const checkDiagonals = (matrix, player) => {
  let diagWin1 = true;
  let diagWin2 = true;
  for(let i =0; i<matrix.length; ++i) {
    if (matrix[i][i] !== player) {
      diagWin1 = false;
    }
    if (matrix[i][matrix.length - i - 1] !== player) {
      diagWin2 = false;
    }
  }
  return diagWin1 || diagWin2;
};
const isFull = (matrix, player) => matrix.flat().every(element => element !== "*");
const win = (matrix, player) => {
  return checkRows(matrix, player) || checkColumns(matrix, player) || checkDiagonals(matrix, player);
}

const matrix = [
  ["*", "*", "*"],
  ["*", "*", "*"],
  ["*", "*", "*"]
];
let player = "X";
let playerMsg = "It's X player turn.";
while(true) {
  const display = displayMatrix(matrix);
  const row = parseInt(prompt(`${playerMsg} \nEnter the row: \n\n ${display}`));
  const col = parseInt(prompt(`${playerMsg} \nEnter the column: \n\n ${display}`));
  const isCorrectRowSize = isNaN(row) || row < 0 || row > matrix.length - 1;
  const isCorrectColSize = isNaN(col) || col < 0 || row > matrix.length - 1;
  if(isCorrectColSize || isCorrectRowSize) {
    alert(`Input is not valid.`);
    continue;
  }
  else if(matrix[row][col] !== "*") {
    alert(`This position is already taken.`);
    continue;
  }
  matrix[row][col] = player;
  const won = win(matrix, player);
  if (won) {
    alert(`The player ${player} won.`);
    break;
  }
  const full = isFull(matrix);
  if (full) {
    alert(`2 Players won.`);
    break;
  }
  player = player === "X" ? "O" : "X";
  playerMsg = `It's ${player} player turn.`;
}

