import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isValid, setisValid] = useState(false);

  /*const handleSubmit = (e) => {
    e.preventDefault();

    if (username === 'Poghos' && password === 'oji154erA!') {
    } else {
      console.log('Invalid credentials');
    }
  };
  */

    const handleLogin = () => {
    const storedUsername = localStorage.getItem('name');
    const storedPassword = localStorage.getItem('pass');


    const isValidCredentials = username === storedUsername && password === storedPassword
    setisValid(isValidCredentials);

    if(isValidCredentials) {
      alert('Succefully entered credentials.')
    } else {
      alert('There is no such account.')
      }
    }

  return (
    <div className="container">
      <h1>Login</h1>
      <form>
        <label htmlFor="username"></label>
        <input
          placeholder="Username"
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label htmlFor="password"></label>
        <input
          placeholder="Password"
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
          <Link to='/home'>
            <button type="submit" onClick={handleLogin} disabled={!isValid}>Login</button>
          </Link>
  
      </form>
    </div>
  );
};

export default Login;

