const dbConfig = require("../config/db.config.js");

const Sequelize = require("sequelize");
const sequelize = new Sequelize(`postgres://postgres:123@localhost:5432/testdb`, {
});

// const sequelize = new Sequelize(
//     `${dbConfig.dialect}://${dbConfig.USER}:${dbConfig.PASSWORD}@${dbConfig.HOST}:${dbConfig.port}/${dbConfig.DB}`,
//   );

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

db.tutorials = require("./tutorial.model.js")(sequelize, Sequelize);
db.users = require("./users.model.js")(sequelize, Sequelize);
module.exports = db;
