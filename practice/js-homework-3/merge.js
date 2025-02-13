const mergeArrays = (arr1, arr2) => {
  let mergedArray = arr1.concat(arr2);
  let seen = {};
  return mergedArray
    .filter((item) => (seen.hasOwnProperty(item) ? false : (seen[item] = true)))
    .sort((a, b) => a - b);
};

console.log(mergeArrays([5, 10, 15, 20], [10, 20, 30, 40]));
