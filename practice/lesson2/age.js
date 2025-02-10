const prompt = require('prompt-sync')();
const checkAge = (age) => {
    if(age<13){
        return "child";
    } else if(age<20){
        return "teenager";
    } else{
        return "adult";
    }
}
const age = parseInt(prompt("Input your age: ")); 
console.log(age>0 ? `You are ${checkAge(age)}` : `Not valid age!`)