const prompt = require('prompt-sync')();

const checkPrimer = (number) => {
    if(number<=1){
        return "The number is not prime.";
    } else {
        let flag = true;
        for(let i = Math.floor(number/2); i>1; i--){
            if(number%i==0){
                flag = false;
                return "The number is not prime.";
            }   
        }
        if(flag){
            return "The number is prime."
        }
    }
}

const number = parseInt(prompt("Input number: "));
console.log(checkPrimer(number));







