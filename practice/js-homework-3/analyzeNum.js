const sum = (arr) => {
  let sum = 0;
  arr.map((elem) => {
    sum += elem;
  });
  return sum;
};

const count = (array) => {
  let count = 0;
  array.forEach((_) => {
    count += 1;
  });
  return count;
};

const analyzeNumbers = (arr) => {
  let obj = {};
  obj.sum = arr.reduce((acc, el) => acc + el, 0);
  obj.avg = sum(arr) / count(arr);
  obj.max = arr.reduce((acc, el) => (acc > el ? acc : el));
  obj.min = arr.reduce((acc, el) => (acc < el ? acc : el));
  obj.evens = arr.filter((el) => el % 2 == 0);
  return obj;
};

console.log(analyzeNumbers([3, 7, 2, 10, 5, 8]));
