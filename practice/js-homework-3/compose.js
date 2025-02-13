function add2(x) {
  return x + 2;
}
function multiply3(x) {
  return x * 3;
}
function compose(func1, func2) {
  return (x) => {
    return func1(func2(x));
  };
}
const composed = compose(add2, multiply3);
console.log(composed(4)); // (4 * 3) + 2 = 14
