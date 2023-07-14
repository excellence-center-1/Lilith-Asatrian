import { useState, useEffect } from "react";
import { Router, Link, useNavigate } from 'react-router-dom';
import bcrypt from 'bcryptjs'

const userRegex = /^[a-zA-Z][a-zA-Z0-9-_]{3,23}$/;
const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;

const Register = () => {

  const navigate = useNavigate();
  const [username, setUser] = useState('');
  const [validUsername, setValidUser] = useState(false);

  const [password, setPass] = useState('');
  const [validPassword, setValidPass] = useState(false);

  useEffect(() => {
    setValidPass(passRegex.test(password));
  }, [password]);

  useEffect(() => {
    setValidUser(userRegex.test(username));
  }, [username]);
 
  const isFormValid = validPassword && validUsername; 
  const handleRegister = async () => {
    if (isFormValid) {
      const hash = bcrypt.hashSync(password, 10)
      const userData = { username: username, password: hash };
      try {
        const response = await fetch('http://localhost:4000/users', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(userData),
        });
        //console.log('aaa');
        if (response.ok) {
        // Handle success
        console.log('User registered successfully');
        setTimeout(() => {
            navigate('/login');
          },1500);

        } else {
            // Handle error
            console.log('Error occurred during registration');
        }
      }

      
      catch (error) {
        console.error('Error:', error);
      }
    } 
    else {
      alert('Please enter valid fields.');
    }
  };
    return <div className="container">
        <h1>Registration</h1>
        <form>
          <label htmlFor="username">
            <span className={validUsername ? "valid" : "hide"}></span>
            <span className={validUsername || !username ? "hide" : "invalid"}></span>
          </label>
          <input
            type="text"
            placeholder="Username"
            id="username"
            autoComplete="off"
            value={username}
            onChange={(e) => setUser(e.target.value)}
            required
            aria-invalid={!validUsername}
          />

          <label htmlFor="password">
            <span className={validPassword ? "valid" : "hide"}></span>
            <span className={validPassword || !password ? "hide" : "invalid"}></span>
          </label>
          <input
            type="password"
            placeholder="Password"
            id="password"
            autoComplete="off"
            value={password}
            onChange={(e) => setPass(e.target.value)}
            required
            aria-invalid={!validPassword}
          />

          <Link to='/login'>
            <button type="submit" onClick = {handleRegister} disabled={!isFormValid}>Register</button>
            <p>Already have an account?</p>
          </Link>   
        </form>
      </div>  
    
};

export default Register;
