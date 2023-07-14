const express = require('express');
const app = express();
const cors = require('cors');
const pgp = require('pg-promise')();
const bcrypt = require('bcryptjs');

app.use(express.json());
app.use(cors());
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');
  next();
});

const db = pgp({
  connectionString: 'postgres://postgres:qwerty@localhost:5432/contact_list',
});

app.post('/users', async (req, res) => {
  try {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await db.query('INSERT INTO users(username, password) VALUES($1, $2)', [username, hashedPassword]);
    res.status(200).json({ message: 'User added successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/login', async (req, res) => {
  try {
    const { username, password } = req.body;

    const user = await db.oneOrNone('SELECT * FROM users WHERE username = $1', [username]);

    if (!user) {
      res.status(401).json({ error: 'Invalid username or password' });
      return;
    }

    const passwordMatch = await bcrypt.compare(password, user.password);

    if (!passwordMatch) {
      res.status(401).json({ error: 'Invalid username or password' });
      return;
    }

    res.status(200).json({ message: 'Login successful', user_id: user.id });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/contacts', async (req, res) => {
  try {
    const result = await db.query('SELECT * FROM contacts');
    const contacts = result.rows;
    res.status(200).json(contacts);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/contacts', async (req, res) => {
  try {
    const { user_id, name, email, phone, profession } = req.body;
    const result = await db.query(
      'INSERT INTO contacts(user_id, name, email, phone, profession) VALUES($1, $2, $3, $4, $5)',
      [user_id, name, email, phone, profession]
    );
    res.status(200).json({ message: 'Contact added successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.delete('/contacts/:id', async (req, res) => {
  try {
    const contactId = req.params.id;
    const result = await db.query('DELETE FROM contacts WHERE id = $1', [contactId]);
    res.status(200).json({ message: 'Contact deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

const PORT = 4000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
