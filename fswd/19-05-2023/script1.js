const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      fetch(url)
        .then(response => {
          if (response.status !== 200) {
            throw new Error(`Failed to fetch data. Response status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          resolve(data);
        })
        .catch(error => {
          reject(error);
        });
    }, 2000);
  });
};

fetchData('users.json')
.then(data => {
  const users = data.users;

  const userId = parseInt(window.prompt('Enter user ID:'));
  const user = users.find(user => user.id === userId);

  if (user) {
    console.log('User:', user);
  } else {
    console.log('User not found.');
  }
})
.catch(error => {
  console.error(error);
});