const express = require('express');
const app = express();

// Set up view engine
app.set('view engine', 'ejs');

// Enable static files
app.use(express.static('public'));

// Enable form processing
app.use(express.urlencoded({ extended: false }));

// In-memory storage for tasks
let tasks = [];

// Route for home page
app.get('/', (req, res) => {
  res.render('index', { task: tasks });
});

// Route for tasks page 
app.get('/tasks', (req, res) => {
  res.render('task', { task: tasks }); 
});

// Retrieve one task by id
app.get('/task/:id', (req, res) => {
  const taskId = req.params.id;
  const task = tasks.find(t => t.id === parseInt(taskId));

  if (task) {
    res.render('task', { task });
  } else {
    res.status(404).send('Task not found');
  }
});

// Add task
app.get('/addTask', (req, res) => {
  res.render('addTask');
});

app.post('/addTask', (req, res) => {
  const { tasks: taskName, priority, deadline } = req.body;

  // Generate a unique ID (you can use a more robust ID generation method)
  const id = tasks.length + 1; 

  const newTask = { id, taskName, priority, deadline };
  tasks.push(newTask);

  res.redirect('/');
});

// Edit task
app.get('/editTask/:id', (req, res) => {
  const taskId = req.params.id;
  const task = tasks.find(t => t.id === parseInt(taskId));

  if (task) {
    res.render('editTask', { task });
  } else {
    res.status(404).send('Task not found');
  }
});

app.post('/editTask/:id', (req, res) => {
  const taskId = req.params.id;
  const { taskName, priority, deadline } = req.body;

  const index = tasks.findIndex(t => t.id === parseInt(taskId));

  if (index !== -1) {
    tasks[index] = { id: taskId, taskName, priority, deadline }; 
    res.redirect('/');
  } else {
    res.status(404).send('Task not found');
  }
});

// Delete task
app.get('/deleteTask/:id', (req, res) => {
  const taskId = req.params.id;
  tasks = tasks.filter(t => t.id !== parseInt(taskId)); 
  res.redirect('/');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));