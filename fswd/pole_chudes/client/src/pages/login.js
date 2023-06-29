import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isValid, setisValid] = useState(false);

  const handleLogin = async () => {
    if (email && password) {
      try {
        const response = await fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, password }),
        });
  
        if (response.ok) {
          console.log('Login successful');
        } else {
          console.log('Login failed');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    } else {
      console.log('Please enter the required fields.');
    }
  };

  return (
    <div className="container">
      <h1>Login</h1>
      <form>
        <label htmlFor="email"></label>
        <input
          placeholder="Email"
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
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
          <Link to='/game'>
            <button type="submit" onClick={handleLogin} disabled={!isValid}>Login</button>
          </Link>
  
      </form>
    </div>
  );
};

export default Login;