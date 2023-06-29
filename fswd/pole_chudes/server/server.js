const express = require('express');
//const { Pool } = require('pg');

const app = express();
const port = 3000;
const db = require('./queries');
const bodyParser = require('body-parser');

app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)

app.post('/users', db.createUser);
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    const query = 'SELECT * FROM users WHERE email = $1 AND pass = $2';
    const { rows } = await pool.query(query, [email, password]);

    if (rows.length > 0) {
      // User found, login successful
      res.status(200).json({ message: 'Login successful' });
    } else {
      // User not found or invalid credentials
      res.status(401).json({ error: 'Invalid credentials' });
    }
  } catch (error) {
    console.error('Error executing query:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});