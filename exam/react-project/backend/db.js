const Pool = require("pg").Pool

const pool = new Pool({
    host: "localhost",
    user: "postgres",
    password: "123",
    database: "posts"
    }
)

module.exports = pool;