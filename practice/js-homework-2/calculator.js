const prompt = require('prompt-sync')();

const calculator = (number1, number2, operation) => {
    switch (operation) {
        case "+":
            return number1+number2;
        case "-":
            return number1-number2;
        case "*":
            return number1*number2;
        case "/":
            return number1/number2;
    }
}

try {
    const number1 = prompt("Input first number: ");
    if(number1 === "" || !isFinite(number1)){
        throw new Error("The input should be valid number!")
    }
    const number2 = prompt("Input second number: ");
    if(number2 === "" || !isFinite(number2)){
        throw new Error("The input should be valid number!")
    }
    const operation = prompt("Input operation: ");
    if(!['+', '-', '/', '*'].includes(operation)){
        throw new Error("No such operation!")
    }
    if(operation=='/' && Number(number2) == 0){
        throw new Error("No division to zero!")
    }
    console.log(`Result: ${calculator(Number(number1), Number(number2), operation)}`);
} catch(error){
    console.error("Error: ", error.message);
}
