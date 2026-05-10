// State Management
let tasks = JSON.parse(localStorage.getItem('final_tasks')) || [];
let currentFilter = 'all';

// DOM Elements
const taskForm = document.querySelector('#task-form');
const taskInput = document.querySelector('#task-input');
const priorityInput = document.querySelector('#priority-input');
const taskList = document.querySelector('#task-list');
const totalDisplay = document.querySelector('#total-tasks');
const completedDisplay = document.querySelector('#completed-tasks');

// Save to LocalStorage
function save() {
  localStorage.setItem('final_tasks', JSON.stringify(tasks));
  updateStats();
}

// Update Statistics
function updateStats() {
  const total = tasks.length;
  const completed = tasks.filter(t => t.completed).length;
  totalDisplay.textContent = `Total: ${total}`;
  completedDisplay.textContent = `Done: ${completed}`;
}

// Render Tasks
function render() {
  taskList.innerHTML = '';
  
  const filteredTasks = tasks.filter(task => {
    if (currentFilter === 'pending') return !task.completed;
    if (currentFilter === 'completed') return task.completed;
    return true;
  });

  filteredTasks.forEach(task => {
    const li = document.createElement('li');
    li.className = `task-item ${task.completed ? 'completed' : ''}`;
    li.innerHTML = `
      <div class="priority-tag ${task.priority}"></div>
      <input type="checkbox" ${task.completed ? 'checked' : ''} onchange="toggleTask(${task.id})">
      <span>${task.text}</span>
      <button class="delete-task" onclick="deleteTask(${task.id})">×</button>
    `;
    taskList.appendChild(li);
  });
}

// Add Task
taskForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const newTask = {
    id: Date.now(),
    text: taskInput.value,
    priority: priorityInput.value,
    completed: false
  };
  tasks.push(newTask);
  save();
  render();
  taskForm.reset();
});

// Toggle Completion
window.toggleTask = (id) => {
  tasks = tasks.map(t => t.id === id ? {...t, completed: !t.completed} : t);
  save();
  render();
};

// Delete Task
window.deleteTask = (id) => {
  tasks = tasks.filter(t => t.id !== id);
  save();
  render();
};

// Filters
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', (e) => {
    document.querySelector('.filter-btn.active').classList.remove('active');
    e.target.classList.add('active');
    currentFilter = e.target.dataset.filter;
    render();
  });
});

// Clear Completed
document.querySelector('#clear-completed').addEventListener('click', () => {
  tasks = tasks.filter(t => !t.completed);
  save();
  render();
});

// Initial Render
render();
updateStats();