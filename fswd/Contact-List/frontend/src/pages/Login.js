import * as React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import { TextField, Typography } from "@mui/material";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
// import axios from "axios";
const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  //const isFormValid = validUsername && validPass && validEmail;

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };
  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/auth/login", {
        method: 'PUT',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();

        localStorage.setItem("userId", data.userId);
        navigate('/contacts');
      } else {
        console.log("Login failed");
      }
    } catch (error) {
      console.error("Error:", error);
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
        Login
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

      <Button
        variant="contained"
        sx={{
          mt: "5%",
          mb: "5%",
          backgroundColor: "green",
          "&:hover": { backgroundColor: "darkgreen" },
        }}
        onClick={handleLogin}
        // disabled={!isFormValid}
      >
        Login
      </Button>
    </Box>
  );
};
export default Login;
