import * as React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { TextField, Typography } from "@mui/material";
import { useState, useEffect } from "react";
import { Link, useNavigate } from 'react-router-dom';
import bcrypt from 'bcryptjs';
import axios from 'axios';

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [validUsername, setValidUser] = useState(false);
  const [password, setPassword] = useState("");
  const [validPass, setValidPass] = useState(false);
  const [email, setEmail] = useState("");
  const [validEmail, setValidEmail] = useState(false);
  const emailRegex = /^\S+@\S+\.\S+$/;
  const usernameRegex = /^[a-zA-Z0-9_-]{3,16}$/;
  const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;

  useEffect(() => {
    setValidUser(usernameRegex.test(username));
  }, [username]);

  useEffect(() => {
    setValidPass(passwordRegex.test(password));
  }, [password]);

  useEffect(() => {
    setValidEmail(emailRegex.test(email)); 
  }, [email]);


  const isFormValid = validUsername && validPass && validEmail;

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  }

  const navigate = useNavigate();
  const handleSignin = async () => {
    if (isFormValid) {
      try {
        const hash = bcrypt.hashSync(password, 10);
        const userData = { username, email, password: hash };
        const response = await fetch('http://localhost:5000/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(userData),
        });
  
        if (response.ok) {
          // Handle successful registration
          console.log('User registered successfully');
          // Redirect to the login page after registration
          navigate('/login');
        } else {
          // Handle registration error
          console.log('Error occurred during registration');
        }
      } catch (error) {
        console.error('Error:', error);
        // Handle the error, e.g., display an error message to the user
      }
    }
  };
  
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        mx: "auto",
        mt: "10%",
        width: "30%",
        backgroundColor: "rgba(1, 40, 4, 0.03)",
        borderRadius: "10%",
      }}
    >
      <Typography variant="h4" sx={{ fontFamily: "Roboto", mt: "5%" }}>
        Sign Up
      </Typography>
      <TextField
        id="outlined-basic"
        label="Username"
        variant="outlined"
        value={username}
        onChange={handleUsernameChange}
        sx={{ mt: "10%" }}
        required
      />
      <TextField
        id="outlined-basic"
        label="Email"
        variant="outlined"
        type="email"
        value={email}
        onChange={handleEmailChange}
        sx={{ mt: "10%" }}
        required
      />
      {/* {validUsername ? null : (
        <Typography variant="body2" sx={{ color: "red", mt: "2%", fontSize: "70%" }}>
          Invalid username. Must be 3-16 characters.
        </Typography>
      )} */}
      <TextField
        id="outlined-basic"
        label="Password"
        type="password"
        variant="outlined"
        value={password}
        onChange={handlePasswordChange}
        sx={{ mt: "10%" }}
        required
      />
      {/* {validPass ? null : (
        <Typography variant="body2" sx={{ color: "red", mt: "2%", fontSize: "70%" }}>
          Password must be at least 8 characters with uppercase,
          lowercase, and a digit.
        </Typography>
      )} */}
      <Button
        variant="contained"
        sx={{
          mt: "5%",
          mb: "5%",
          backgroundColor: "green",
          "&:hover": { backgroundColor: "darkgreen" },
        }}
        onClick={handleSignin}
        disabled={!isFormValid}
      >
        Sign Up
      </Button>
      <Link to='/login'><p>Already have an account?</p></Link>
    </Box>
  );
};
export default SignUp;
