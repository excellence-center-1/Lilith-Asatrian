const helper = (preObj, suffix, res) => {
  let key;
  for (let x in preObj) {
    if (suffix !== "") {
      key = suffix + "." + x;
    } else {
      key = x;
    }

    if (typeof preObj[x] !== "object") {
      res[key] = preObj[x];
    } else {
      helper(preObj[x], key, res);
    }
  }
};
const flattenObject = (myObj) => {
  let newObj = {};
  helper(myObj, "", newObj);
  return newObj;
};

const data = {
  user: {
    name: "John",
    address: { city: "NY", zip: 10001 },
  },
  age: 30,
};

console.log(flattenObject(data));
