const express = require('express');
const app = express();
const tasksRoutes = require('./routes/tasks')
const connectDB = require('./db/connect')
require('dotenv').config()
const notFound = require('./middleware/not-found')
const errorHandlerMiddleware = require('./middleware/error-handler')
//middleware
app.use(express.static('./public'))
app.use(express.json())

//routes
app.use('/api/v1/tasks', tasksRoutes)

app.use(notFound)
app.use(errorHandlerMiddleware)

const port = 5000

const start = async () => {
    try {
        await connectDB(process.env.MONGO_URI)
        app.listen(port, console.log(`Server is listening on port ${port}...`))
    } catch (error) {
        console.log(error);
    }
}
start()