// This file contains the JavaScript code for the To-do List app. It handles user interactions, such as adding and deleting tasks, and updates the DOM accordingly.

document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    addTaskBtn.addEventListener('click', function() {
        const taskText = taskInput.value.trim();
        if (taskText) {
            const li = document.createElement('li');
            li.className = 'bg-pastel-blue p-2 rounded-md flex justify-between items-center mb-2';
            li.textContent = taskText;

            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = '삭제';
            deleteBtn.className = 'bg-pastel-red text-white py-1 px-3 rounded-md hover:bg-red-600';
            deleteBtn.addEventListener('click', function() {
                li.remove();
            });

            li.appendChild(deleteBtn);
            taskList.appendChild(li);
            taskInput.value = '';
        }
    });
});