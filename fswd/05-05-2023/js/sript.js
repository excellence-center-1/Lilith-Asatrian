let input1 = prompt("What is your name?")
let input2 = parseInt(prompt("What is your age?"))
if(input2 < 0 || isNaN(input2)) {
  alert(`Please, enter a valid age.`);
}
else {
  switch (true) {
    case input2 <= 12:
      alert(`Welcome ${input1}! You are in childhood.`);
      break;
    case input2 <= 19:
      alert(`Welcome ${input1}! You are a teenager.`);
      break;
    case input2 <= 29:
      alert(`Welcome ${input1}! You are a young adult.`);
      break;
    case input2 <= 59:
      alert(`Welcome ${input1}! You are an adult.`);
      break;    
    default:
      alert(`Welcome ${input1}! You are a senior.`);
      break;
  }
}

