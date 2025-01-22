const express = require('express');
const mysql = require('mysql2');
const app = express();

// Create MySQL connection
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'c237_tasklistapp1'
});
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// Set up view engine
app.set('view engine', 'ejs');

// Enable static files
app.use(express.static('public'));

// Enable form processing
app.use(express.urlencoded({ extended: false }));

// Route for home page
app.get('/', (req, res) => {
    const sql = 'SELECT * FROM task';

    connection.query(sql, (error, results) => {
        if (error) {
            console.error('Database query error:', error.message);
            return res.status(500).send('Error Retrieving tasks');
        }

        res.render('index', { task: results });
    });
});

// Route for tasks page
app.get('/tasks', (req, res) => {
    const sql = 'SELECT * FROM task';

    connection.query(sql, (error, results) => {
        if (error) {
            console.error('Database query error:', error.message);
            return res.status(500).send('Error Retrieving tasks');
        }

        res.render('task', { task: results });
    });
});

// Retrieve one task by id
app.get('/task/:id', (req, res) => {
    const taskId = req.params.id;
    const sql = 'SELECT * FROM task WHERE taskId = ?';

    connection.query(sql, [taskId], (error, results) => {
        if (error) {
            console.error('Database query error:', error.message);
            return res.status(500).send('Error Retrieving task by ID');
        }

        if (results.length > 0) {
            res.render('task', { task: results[0] });
        } else {
            res.status(404).send('Task not found');
        }
    });
});

// Add task
app.get('/addTask', (req, res) => {
    res.render('addTask');
});

app.post('/addTask', (req, res) => {
    const { tasks, priority, deadline } = req.body;

    console.log('Received data:', { tasks, priority, deadline });

    const sql = 'INSERT INTO task (tasks, priority, deadline) VALUES (?, ?, ?)';

    connection.query(sql, [tasks, priority, deadline], (error, results) => {
        if (error) {
            console.error("Error adding task:", error);
            res.status(500).send('Error adding task');
        } else {
            res.redirect('/');
        }
    });
});


// Edit task
app.get('/editTask/:id', (req,res) => {
    const taskId = req.params.id;
    const sql = 'SELECT * FROM task where taskId = ?';
    connection.query( sql, [taskId], (error, results) => {
        if (error) {
            console.error('Database query error:', error.message);
            return res.status(500).send('Error retrieving task by ID');
        }
        if (results.length > 0) {
            res.render('editTask', { task: results[0] });
        } else {
            res.status(404).send('Task not found');
        }
    });
});

// Update task
app.post('/editTask/:id', (req,res) => {
    const taskId = req.params.id;
    const { tasks, priority, deadline } = req.body;
    const sql = 'UPDATE task SET tasks = ? , priority = ?, deadline = ? WHERE taskId = ?';

    connection.query( sql , [tasks, priority, deadline, taskId], (error, results) => {
        if (error) {
            console.error("Error updating task:", error);
            res.status(500).send('Error updating task');
        } else {
            res.redirect('/');
        }
    });
});

// Delete task
app.get('/deleteTask1/:id', (req, res) => {
    const taskId = req.params.id;
    const sql = 'DELETE FROM task WHERE taskId = ?';
    connection.query( sql, [taskId], (error, results) => {
        if (error) {
            console.error("Error deleting task:", error);
            res.status(500).send('Error deleting task');
        } else {
            res.redirect('/');
        }
    });
});


  


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));