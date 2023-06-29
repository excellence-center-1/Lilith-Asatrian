const Pool = require('pg').Pool

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'pole_chudes',
  password: 'qwerty',
  port: 5432,
});

const createUser = (request, response) => {
  const { email, pass } = request.body;

  pool.query('INSERT INTO users (email, pass) VALUES ($1, $2)', [email, pass], (error, results) => {
    if (error) {
      throw error;
    }
    response.status(201).send(`User added with ID: ${results.insertId}`);
  });
};

export default createUser;