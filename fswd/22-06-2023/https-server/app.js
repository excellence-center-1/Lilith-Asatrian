const https = require('https'); //requiring in-built https
//for get and post
const express = require('express');
const app = express(); 
//for using local files
const fs = require('fs');
//for taking body form in parsed way
const bodyParser = require('body-parser');

//express uses bodyparser as middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get("/", function(req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.post("/mssg", function (req, res) {
  console.log(req.body);
  res.redirect("/");
});

const options = {
  key: fs.readFileSync("server.key"),
  cert: fs.readFileSync("server.cert"),
};

//pass option and app objects
https.createServer(options, app)
.listen(3000, function (req, res) {
  console.log("Server started.");
});
