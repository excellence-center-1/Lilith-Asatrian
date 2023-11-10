module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.addColumn('tutorials', 'userId', {
      type: Sequelize.INTEGER,
      references: {
        model: 'users',
        key: 'id',
      },
      onUpdate: 'CASCADE',
      onDelete: 'SET NULL',
    });
  },

  down: async (queryInterface) => {
    await queryInterface.removeColumn('tutorials', 'userId');
  },
};