// const sum = (arr) => {
//   let sum = 0;
//   arr.map((elem) => {
//     sum += elem;
//   });
//   return sum;
// };

const sum = (arr) => {
  return arr.reduce((acc, el) => acc+el, 0);
}
const analyzeNumbers = (arr) => {
  let obj = {};
  obj.sum = sum(arr);
  obj.avg = sum(arr) / arr.length;
  obj.max = arr.reduce((acc, el) => (acc > el ? acc : el));
  obj.min = arr.reduce((acc, el) => (acc < el ? acc : el));
  obj.evens = arr.filter((el) => !(el % 2));
  return obj;
};

console.log(analyzeNumbers([3, 7, 2, 10, 5, 8]));
