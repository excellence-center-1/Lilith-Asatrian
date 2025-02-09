import { React, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios'
import '../styles/login.css'
import MyInput from "../UI/input/input";
import MyButton from "../UI/input/button/button";
axios.defaults.withCredentials = true;
const Login = () => {
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    const handleSubmit = async(e) => {
        e.preventDefault();
        try{
            const user = await axios.post("http://localhost:5000/api/login", {
                email: login,
                password: password
        })
            console.log(user.data);
            navigate("/posts");
        } catch(error) {
            console.error(error.message);
        } 
    }
    return(
        <div className="box">
            <h2>Login</h2>
            <MyInput type="text" placeholder="Email" value={login} onChange = {(e) => setLogin(e.target.value)}/>
            <MyInput 
                type="password"
                placeholder="Password"
                value={password}
                onChange={e=>setPassword(e.target.value)}
            />
            <MyButton onClick = {handleSubmit}>Submit</MyButton>
        </div>
    );
}

export default Login;