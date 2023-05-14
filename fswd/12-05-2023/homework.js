/* Task 1: Write a function that takes in an array of numbers 
and returns the sum of all the even numbers in the array. */
const myarr = [1,2,6,8,3,9];
const evenSum = function(arr) {
  let sum = 0;
  arr.forEach(elem => {
    if(elem % 2 == 0) {
      sum += elem;
    }
  });
  return sum;
}
//const sum = myarr.reduce((acc, curr) => curr % 2 === 0 ? acc + curr : acc, 0);
console.log(`The sum of [${myarr}] array is ${evenSum(myarr)}.`);

/* Task 2: Write a function that takes in a string 
and returns the string reversed. */
let myStr = "Lilith"
const reverseString = function(str) {
  return str.split('').reverse().join('');
}
console.log(`The reversed version of ${myStr} is ${reverseString(myStr)}.`);

/* Task 3: Write a function that takes in an array of strings 
and returns a new array with all the strings capitalized. */
const arr = ['l', 'dd', 'rD'];
const capitalized = function(arr) {
  newarr = [];
  arr.forEach(elem => {
    newarr.push(elem.toUpperCase());
  });
  return newarr;
}
console.log(capitalized(arr));