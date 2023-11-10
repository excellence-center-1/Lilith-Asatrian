module.exports = {
  up(queryInterface, Sequelize) {
    return Promise.all([
      queryInterface.addColumn(
        'tutorials', 
        'magazine', 
        {
          type: Sequelize.STRING,
          allowNull: true,
        },
      ),
      queryInterface.addColumn(
        'tutorials',
        'books',
        {
          type: Sequelize.STRING,
          allowNull: true,
        },
      ),
    ]);
  },

  down(queryInterface, Sequelize) {

    return Promise.all([
      queryInterface.removeColumn('tutorials', 'magazine'),
      queryInterface.removeColumn('tutorials', 'books'),
    ]);
  },
};
