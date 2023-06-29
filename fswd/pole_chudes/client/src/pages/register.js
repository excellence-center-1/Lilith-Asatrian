import { useState, useEffect } from "react";
import {Link} from 'react-router-dom'

const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
const emailRegex = /^[a-zA-Z][a-zA-Z0-9-_.]{0,23}@[a-zA-Z0-9-]{2,}\.[a-zA-Z]{2,}$/;

const Register = () => {

  const [pass, setPass] = useState('');
  const [validPass, setValidPass] = useState(false);

  const[email, setEmail] = useState('');
  const[validEmail, setValidEmail] = useState(false);

  useEffect(() => {
    setValidPass(passRegex.test(pass));
  }, [pass]);

  useEffect(() => {
    setValidEmail(emailRegex.test(email));
  }, [email]);
 
  const isFormValid = validPass && validEmail; 
  const handleRegister = async () => {
    if (isFormValid) {
      try {
        await fetch('/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email: email, pass: pass }),
        });
      } 
      catch (error) {
        console.error('Error:', error);
      }
    } 
    else {
      alert('Please enter the required fields.');
    }
  };

  return (
    <div className="container">
      <h1>Registration</h1>
      <form>

        <label htmlFor="email">
          <span className={validEmail ? "valid" : "hide"}></span>
          <span className={validEmail || !email ? "hide" : "invalid"}></span>
        </label>
        <input
          type="email"
          placeholder="Email"
          id="email"
          autoComplete="off"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          aria-invalid={!validEmail}
        />

        <label htmlFor="password">
          <span className={validPass ? "valid" : "hide"}></span>
          <span className={validPass || !pass ? "hide" : "invalid"}></span>
        </label>
        <input
          type="password"
          placeholder="Password"
          id="password"
          autoComplete="off"
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          required
          aria-invalid={!validPass}
        />

        <Link to='/login'>
          <button type="submit" onClick = {handleRegister} disabled={!isFormValid}>Register</button>
          <p>Already have an account?</p>
        </Link>
        
      </form>
    </div>
  );
};

export default Register;