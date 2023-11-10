const User = require('./users.model');

module.exports = (sequelize, Sequelize) => {
  const Tutorial = sequelize.define("tutorial", {
    title: {
      type: Sequelize.STRING
    },
    description: {
      type: Sequelize.STRING
    },
    published: {
      type: Sequelize.BOOLEAN
    },
    magazine: {
      type: Sequelize.STRING
    },
    books: {
      type: Sequelize.STRING
    }
  });

//   Tutorial.belongsTo(User, { foreignKey: 'userId' });

  return Tutorial;
};
