const getFormvalue = (event) => {
  event.preventDefault();
  const fname = document.forms["form1"]["fname"].value;
  const lname = document.forms["form1"]["lname"].value;
  console.log(fname, lname);
};
