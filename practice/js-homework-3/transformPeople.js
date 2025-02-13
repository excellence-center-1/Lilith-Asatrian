const transformPeople = (people) => {
  for (let index = 0; index < people.length; index++) {
    people[index]["name"] = people[index]["name"].toUpperCase();
    people[index]["age"] += 5;
    people[index]["city"] = people[index]["city"].split("").reverse().join("");
  }
  return people;
};

const people = [
  { name: "Alice", age: 25, city: "New York" },
  { name: "Bob", age: 30, city: "Los Angeles" },
];

console.log(transformPeople(people));

