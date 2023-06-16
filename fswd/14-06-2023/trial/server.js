const express = require('express');
const fs = require('fs');

const app = express();
const port = 3002;

app.get('/listUsers', (req, res) => {
  fs.readFile( __dirname + "/" + "users.json", 'utf8', (err, data) => {
    res.end(JSON.stringify(data));
 });
})

app.post('/addUser', (req, res) => {
  fs.readFile(__dirname + "/" + "users.json", 'utf8', (err, data) => {    
    const users = JSON.parse(data); //generates js object
    const newUser = {
      "name": "manuk",
      "password": "password4",
      "profession": "cook",
      "id": 4
    };  

    users["user4"] = newUser; //adds the newUser to users object
    const updatedData = JSON.stringify(users, null, 100); // Indentation with 2 spaces

    fs.writeFile(__dirname + "/" + "users.json", updatedData, 'utf8', (err) => {
      res.end(updatedData);
    });  
  }
  );
});  

app.delete('/deleteUser/:id', (req) => {
  const userId = req.params.id;
  fs.readFile( __dirname + '/' + "users.json", 'utf8', (err, data) => {
    const users = JSON.parse(data);
    if( users.hasOwnProperty(userId)) {
      delete users[userId];
      const updatedData = JSON.stringify(users);

      fs.writeFile(__dirname + "/" + "users.json", updatedData, 'utf8', (err) => {
        res.setHeader('Content-Type', 'application/json');
        res.end(updatedData);
      })
    } else {
      console.log("Such id is not found.");
    }

  })
})

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});