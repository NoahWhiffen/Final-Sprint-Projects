// Intro to Javascript - Final Sprint
// Author: Noah Whiffen
// Dates: July 30, 2024 - July 31, 2024

// You may have to run this with Live Server. The CORS policy wouldn't let me run the program and this was the
// only way I could find to pass it.

const jsonFile = "data.json";

// Program functions.

function getTotal(data) {
    return `The total number of records is ${data.length}.`;
}

function numOfStudents(data) {
    const studentCount = data.filter(record => record.student).length;
    return `The number of students is ${studentCount}.`;
}

function listCourses(data) {
    const course = data
        .filter(record => record.courses) // Only include records with courses.
        .flatMap(record => record.courses); // Flatten array to courses.
    
    const courses = [...new Set(course)]; // This is to remove duplicates.

    return `The list of courses taken by members of the Smith Family: ${courses.join(', ')}`;
}

fetch(jsonFile)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data.forEach(record => {
        console.log(`ID: ${record.id}, Name: ${record.name}`)
        });
        console.log(getTotal(data));
        console.log(numOfStudents(data));
        console.log(listCourses(data));
        document.getElementById('dataContainer').textContent = JSON.stringify(data, null, 2);
    });

