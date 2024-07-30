// Intro to Javascript - Final Sprint

document.addEventListener('DOMContentLoaded', () => {
    fetch('data.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(person => {
            
        });