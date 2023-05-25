function startGame() {
  document.addEventListener("DOMContentLoaded", function () {
    const dimension = parseInt(prompt("Enter the dimension of the board (e.g., 3 for 3x3):"));
    const board = document.getElementById("board");
    let currentPlayer = "X";
    let gameBoard = Array.from(Array(dimension), () => Array(dimension).fill(""));

    createCells();

    function createCells() {
      for (let i = 0; i < dimension; i++) {
        const row = document.createElement("div");
        row.className = "row";
        for (let j = 0; j < dimension; j++) {
          const cell = document.createElement("div");
          cell.className = "cell";
          cell.addEventListener("click", function () {
            makeMove(i, j);
          });
          row.appendChild(cell);
        }
        board.appendChild(row);
      }
    }

    function makeMove(row, col) {
      if (gameBoard[row][col] === "") {
        gameBoard[row][col] = currentPlayer;
        updateBoard();
        checkWinner();
        currentPlayer = currentPlayer === "X" ? "O" : "X";
      }
    }

    function updateBoard() {
      const cells = document.getElementsByClassName("cell");
      let cellIndex = 0;
      for (let i = 0; i < dimension; i++) {
        for (let j = 0; j < dimension; j++) {
          cells[cellIndex].textContent = gameBoard[i][j];
          cellIndex++;
        }
      }
    }

    function checkWinner() {
      const winningCombos = getWinningCombos();

      for (let combo of winningCombos) {
        let winnerFound = true;
        for (let [row, col] of combo) {
          if (gameBoard[row][col] !== currentPlayer) {
            winnerFound = false;
            break;
          }
        }
        if (winnerFound) {
          alert(`Player ${currentPlayer} wins!`);
          resetGame();
          return;
        }
      }

      if (isBoardFull()) {
        alert("It's a draw!");
        resetGame();
      }
    }

    function getWinningCombos() {
      const winningCombos = [];

      for (let i = 0; i < dimension; i++) {
        const rowCombo = [];
        const colCombo = [];
        for (let j = 0; j < dimension; j++) {
          rowCombo.push([i, j]);
          colCombo.push([j, i]);
        }
        winningCombos.push(rowCombo, colCombo);
      }

      const diagonal1 = [];
      const diagonal2 = [];
      for (let i = 0; i < dimension; i++) {
        diagonal1.push([i, i]);
        diagonal2.push([i, dimension - 1 - i]);
      }
      winningCombos.push(diagonal1, diagonal2);

      return winningCombos;
    }

    function isBoardFull() {
      for (let i = 0; i < dimension; i++) {
        for (let j = 0; j < dimension; j++) {
          if (gameBoard[i][j] === "") {
            return false;
          }
        }
      }
      return true;
    }

    function resetGame() {
      currentPlayer = "X";
      gameBoard = Array.from(Array(dimension), () => Array(dimension).fill(""));
      updateBoard();
    }
  });
}
startGame();
