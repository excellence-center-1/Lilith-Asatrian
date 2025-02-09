const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const pool = require('../db');
const config = require('../config')

const register = async(req, res) => {
    try {
        const salt = await bcrypt.genSalt(10);
        const hashpass = await bcrypt.hash(req.body.password, salt);1
        const userTypeResult = await pool.query('SELECT * FROM user_types WHERE id=$1', [req.body.user_type_id || 1]);
        if(userTypeResult.rowCount === 0){
            res.status(400).send("No such user exist");
        }
        const result = await pool.query('INSERT INTO users(name, email, password, user_type_id) VALUES($1, $2, $3, $4) RETURNING id', [req.body.name, req.body.email, hashpass, req.body.user_type_id || 1])
        const userId = result.rows[0].id;

        const payload = {id: userId, user_type_id: req.body.user_type_id || 1};
        const token = jwt.sign(payload, config.TOKEN_SECRET, {expiresIn: '1h'});
        res.status(200).send({token});
    } catch (error) {
       console.error(error.message)
       res.send('Server error') 
    }
}

const login = async(req, res) => {
    try {
        const {email, password} = req.body;
        const result = await pool.query('SELECT * FROM users WHERE email=$1', [email]);
        if(result.rowCount === 0){
            return res.status(400).send("No such user exist with this email");
        }
        const validPass = await bcrypt.compare(password, result.rows[0].password);
            
        if(!validPass) {
            return res.status(401).send("Wrong password is entered");
        } 

        let payload = {id: result.rows[0].id, user_type_id: result.rows[0].user_type_id};
        const token = await jwt.sign(payload, config.TOKEN_SECRET);

        // res.status(200).header("auth-token", token).send({token})
        res.cookie('token', token, {httpOnly: true}).status(200).send({message: "Login succesfully!!"});
    } catch (error) {
        console.error(error.message);
        res.status(500).send("Server error");
    }
}

module.exports = {register, login}


