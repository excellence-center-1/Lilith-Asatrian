const prompt = require('prompt-sync')();
const checkNum = (number) => {
    if(number>0){
        return "positive";
    } else if(number<0){
        return "negative";
    } else{
        return "zero"
    }
}

const number = parseInt(prompt("Input number: "));
console.log(`Your number is ${checkNum(number)}`);

