const url = 'http://127.0.0.1:8081/';
fetch('users.json')
  .then(response => {
    if (response.status !== 200) {
      throw new Error('Failed to fetch data. Response status: ' + response.status);
    }
    return response.json();
  })
  .then(data => {
    const users = data.users;

    const userId = parseInt(window.prompt('Enter user ID:')); 
    const user = users.find(user => user.id === userId);

    if (user) {
      console.log('User:', user);
    } 
    else {
      console.log('User not found.');
    }
  })
  .catch(error => {
    console.error(error);
  });
