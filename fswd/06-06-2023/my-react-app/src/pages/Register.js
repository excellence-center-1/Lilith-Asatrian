import { useState, useEffect } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import {Link} from 'react-router-dom'

const userRegex = /^[a-zA-Z][a-zA-Z0-9-_]{3,23}$/;
const passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
const emailRegex = /^[a-zA-Z][a-zA-Z0-9-_]{0,23}@[a-zA-Z0-9-]{2,}\.[a-zA-Z]{2,}$/;

const Register = () => {

  const [name, setName] = useState('');
  const [validName, setValidName] = useState(false);

  const [pass, setPass] = useState('');
  const [validPass, setValidPass] = useState(false);

  const[email, setEmail] = useState('');
  const[validEmail, setValidEmail] = useState(false);

  const [gender, setGender] = useState('');
  const [isGenderSelected, setIsGenderSelected] = useState(false);

  const [selectedDate, setSelectedDate] = useState(null);
  const [validDate, setValidDate] = useState(false);

  //const [registrationComlete, setRegistrationComplete] = useState(false);

  /* Meant to check just for me
  const handleSubmit = (e) => {
    e.preventDefault();
    if (validName && validPass & validEmail) {
      console.log('Registration submitted');
    } 
    else {
      console.log('Invalid form submission');
    }
     //history.push('/login');
  };
  */

  useEffect(() => {
    setValidName(userRegex.test(name));
  }, [name]);

  useEffect(() => {
    setValidPass(passRegex.test(pass));
  }, [pass]);

  useEffect(() => {
    setValidEmail(emailRegex.test(email));
  }, [email]);

  const handleGenderChange = (e) => {
    setGender(e.target.value);
    setIsGenderSelected(true);
  }

  const handleDateChange = (date) => {
    setSelectedDate(date);
    setValidDate(date !== null);
  };
 
  const isFormValid = validName && validPass && validEmail && isGenderSelected && validDate;

  const handleRegister = () => {
    if(isFormValid) {
      localStorage.setItem('name', name);
      localStorage.setItem('pass', pass);
      //setRegistrationComplete(true);
    } else {
      alert('Please enter the required fields.')
    }
  }

  return (
    <div className="container">
      <h1>Registration</h1>
      <form>
        <label htmlFor="username">
          <span className={validName ? "valid" : "hide"}></span>
          <span className={validName || !name ? "hide" : "invalid"}></span>
        </label>
        <input
          type="text"
          placeholder="Username"
          id="username"
          //ref={userRef}
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
          placeholder="Password"
          id="password"
          //ref={passRef}
          autoComplete="off"
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          required
          aria-invalid={!validPass}
        />

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

        <div className="gender-container">
        <label className="gender-lable" htmlFor="gender">Gender :</label>
          <div style = {{display: 'flex'}}> 
            <label>
              <input
                className="gender-input"
                type="radio"
                name="gender"
                value="male"
                checked={gender === 'male'}
                onChange={handleGenderChange}
              />
              Male
            </label>
            <label>
              <input
                className="gender-input"
                type="radio"
                name="gender"
                value="female"
                checked={gender === 'female'}
                onChange={handleGenderChange}
              />
              Female
            </label>
            <label>
              <input
                className="gender-input"
                type="radio"
                name="gender"
                value="other"
                checked={gender === 'other'}
                onChange={handleGenderChange}
              />
              Other
            </label>
          </div>
        </div>

        <div className="dob-container">
          <label className="dob-label" htmlFor="dob">Date of Birth:</label>
          <DatePicker
            className="dob-select"
            id="dob"
            selected={selectedDate}
            onChange={handleDateChange}
            placeholderText="Select date"
            showYearDropdown
            scrollableYearDropdown
            yearDropdownItemNumber={100}
            required
          />
        </div>


        <Link to='/login'>
          <button type="submit" onClick = {handleRegister} disabled={!isFormValid}>Register</button>
        </Link>
        
      </form>
    </div>
  );
};

export default Register;
