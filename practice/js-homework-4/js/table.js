const createTable = () => {
  const row = parseInt(prompt("Input the number of rows"));
  const column = parseInt(prompt("Input the number of columns"));

  if (isNaN(row) || isNaN(column) || row <= 0 || column <= 0) {
    alert("Enter valid data");
    return;
  }

  let table = document.getElementById("myTable");

  for (let i = 0; i < row; i++) {
    let newRow = table.insertRow(i);
    for (let j = 0; j < column; j++) {
      let newCell = newRow.insertCell(j);
      newCell.textContent = `Row-${i} Column-${j}`;
    }
  }
  
};
