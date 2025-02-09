const express = require('express')
const cors = require('cors')
const app = express()
const port = 5000

app.use(express.json());
app.use(cors({
    origin: "http://localhost:3000",
    credentials: true
}))

authRoutes = require('./routers/index')

app.use('/api', authRoutes)

app.listen(port, () => {
    console.log(`Server is running on port ${port}`)  
})