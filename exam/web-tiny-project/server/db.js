const Pool = require("pg").Pool

const pool = new Pool({
    host: "localhost",
    user: "postgres",
    password: "123",
    database: "todo_db"
    }
)

module.exports = pool;