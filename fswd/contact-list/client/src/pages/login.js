import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
//import ContactList from './ContactList';
import ContactItem from './ContactItem';

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [userId, setUserId] = useState(null);
  //const [isValid, setisValid] = useState(false);

  /*const handleSubmit = (e) => {
    e.preventDefault();

    if (username === 'Poghos' && password === 'oji154erA!') {
    } else {
      console.log('Invalid credentials');
    }
  };
  */

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:4000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        // Handle successful login
        const data = await response.json();
        setUserId(data.userId); 
        console.log('User logged in successfully, userId:', userId);
        setTimeout(() => {
          navigate('/ContactItem');
          <ContactItem userId={userId}/>
        }, 1500);
        
      } else {
        // Handle login error
        console.log('Login failed');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  //const storedUsername = localStorage.getItem('name');
  //const storedPassword = localStorage.getItem('pass');
  //const isValidCredentials = username === storedUsername && password === storedPassword

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
          <Link to='/ContactItem'>
            <button type="submit" onClick={handleLogin} >Login</button>
          </Link>
          
          
      </form>
    </div>
  );
};

export default Login;

