const express = require('express')
const app = express()
const port = 5000
const cors = require('cors')
const pool = require('./db')

app.use(cors())
app.use(express.json())

// app.get('/', (req, res) => {
//     res.send('Hello world')
// })

//create a todo
app.post('/todos', async(req, res) => {
    try {
        const {description} = req.body;
        const newTodo = await pool.query('INSERT INTO todo(description) VALUES($1) RETURNING *', [description]);
        res.json(newTodo.rows[0]);
    } catch(err) {
        console.error(err.message)
        res.status(500).send('Server error')
    }
})
//get a todo

app.get('/todos/:id', async (req, res) => {
    try {
        const {id} = req.params
        const todo = await pool.query("SELECT * FROM todo WHERE id=$1", [id])
        res.json(todo.rows[0])
    } catch(err) {
        console.error(err.message);
        res.status(500).send("Server error");
    }
})

//update a todo
app.put('/todos/:id', async(req, res) => {
    try {
        const {id} = req.params
        const {description} = req.body
        await pool.query('UPDATE todo set description=$1 WHERE id=$2',[description, id])
        res.json("Updated todo!")
    } catch (err) {
        console.error(err.message)
        res.status(500).send('Server error')
    }
})
//delete a todo
app.delete('/todos/:id', async(req, res) => {
    try {
        const {id} = req.params
        await pool.query('DELETE from todo where id=$1', [id])
        res.json("Deleted the row!")
    } catch (error) {
        console.error(error.message)
        res.status(500).send('Server error')
    }
})
//get all todos

app.get('/todos', async(req, res) => {
    try {
        const todos = await pool.query("Select * from todo");
        res.json(todos.rows);
    } catch(err){
        console.error(err.message)
        res.status(500).send('Server error')
    }
})

app.listen(port, ()=> {
    console.log(`Server is running on port ${port}`)
})