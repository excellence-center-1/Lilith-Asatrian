let displayMatrix = function(matrix) {
  return matrix[0].join("  ") + 
     "\n" + 
     matrix[1].join("  ") + 
     "\n" + 
     matrix[2].join("  ");
 };
 
 let win = function(matrix, player) {

 	//check rows
 	for(let i = 0; i < matrix.length; ++i) {
  	let rowWin = true;
    for(let j = 0; j < matrix.length; ++j) {
    	if(matrix[i][j] !== player){
      	rowWin = false;
        break;
      }
    }
    if(rowWin) {
    	return true;
    }
  }
  
  //check columns
 	for(let i = 0; i < matrix.length; ++i) {
  	let colWin  = true;
    for(let j = 0; j < matrix.length; ++j) {
    	if(matrix[j][i] !== player){
      	colWin = false;
        break;
      }
    }
    if(colWin) {
    	return true;
    }
  }
  
  //check diagonals
  let diagWin1 = true;
  let diagWin2 = true;
  for(let i = 0; i < matrix.length; ++i) {
  	if(matrix[i][i] !== player) {
    	diagWin1 = false;
    }
    if(matrix[i][matrix.length-i-1] !== player) {
    	diagWin2 = false;
    }
  }
  if(diagWin1 || diagWin2) {
    	return true;
  }
  return false;
 }

 let isFull = function(matrix) {
  if(matrix.flat().every(element => element !== "*")){
    return true;
  }
  return false;
 }
 
 let matrix = [
   ['*', '*', '*'],
   ['*', '*', '*'],
   ['*', '*', '*']
 ]; 
 
 let player = "X";
 let playerMsg = "It's X player turn.";

 while(true){
     let display = displayMatrix (matrix);
     let row = parseInt(prompt(playerMsg + "\nEnter the row: \n\n" + display));
     let col = parseInt(prompt(playerMsg + "\nEnter the column: \n\n" + display));
     if (isNaN(row) || isNaN(col) || row < 0 || row > 2 || col < 0 || col > 2 || matrix[row][col] !== "*") {
      alert(`Not a valid move. ${player} loses.`);
      continue;
    }
    
     matrix[row][col] = player;
     const won = win(matrix, player);
     if(won){
     	alert(`The player ${player} won.`);
      break;
     }
     const full = isFull(matrix);
     if(full){
      alert(`2 Players won.`);
      break;
     }
     if(player === "X") {
       player = "O";
       playerMsg = "It's O player turn.";

     }
     else {
       player = "x";
       playerMsg = "It's X player turn."
     }
 }