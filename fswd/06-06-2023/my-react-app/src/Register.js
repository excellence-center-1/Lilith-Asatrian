import { useRef, useState, useEffect } from "react";
import { useHistory } from "react-router-dom"
const userRegex = /^[a-zA-Z][a-zA-Z0-9-_]{3,23}$/;
const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;

const Register = () => {
  const history = useHistory();
  const userRef = useRef();
  const passRef = useRef();
  const [name, setName] = useState('');
  const [validName, setValidName] = useState(false);

  const [pass, setPass] = useState('');
  const [validPass, setValidPass] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validName && validPass) {
      console.log('Registration submitted');
    } 
    else {
      console.log('Invalid form submission');
    }
    history.push('/login')
  };

  useEffect(() => {
    setValidName(userRegex.test(name));
  }, [name]);

  useEffect(() => {
    setValidPass(passRegex.test(pass));
  }, [pass]);

  return (
    <div>
      <h1>Registration</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">
          <span className={validName ? "valid" : "hide"}></span>
          <span className={validName || !name ? "hide" : "invalid"}></span>
        </label>
        <input
          type="text"
          placeholder="Username"
          id="username"
          ref={userRef}
          autoComplete="off"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          aria-invalid={!validName}
        />

        <label htmlFor="password">
          <span className={validPass ? "valid" : "hide"}></span>
          <span className={validPass || !pass ? "hide" : "invalid"}></span>
        </label>
        <input
          type="password"
          placeholder="password"
          id="password"
          ref={passRef}
          autoComplete="off"
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          required
          aria-invalid={!validPass}
        />

        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
