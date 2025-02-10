const prompt = require('prompt-sync')();
const calculator = (number1, number2, operation) => {
    switch (operation) {
        case "+":
            return number1+number2;
            break;
        case "-":
            return number1-number2;
            break;
        case "*":
            return number1*number2;
            break;
        case "/":
            return number1/number2;
            break;
    }
}

try{
    const number1 = parseFloat(prompt("Input first number: "));
    if(isNaN(number1)){
        throw new Error("The input should be number!")
    }
    const number2 = parseFloat(prompt("Input second number: "));
    if(isNaN(number2)){
        throw new Error("The input should be number!")
    }
    const operation = prompt("Input operation: ");
    if(!['+', '-', '/', '*'].includes(operation)){
        throw new Error("No such operation!")
    }
    if(operation=='/' && number2==0){
        throw new Error("No division to zero!")
    }
    console.log(`Result: ${calculator(number1, number2, operation)}`);
} catch(error){
    console.error("Error: ", error.message);
}
