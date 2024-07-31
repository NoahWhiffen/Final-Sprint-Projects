// Intro to Javascript - Final Sprint

const jsonFile = "data.json";

fetch(jsonFile)
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });

jsonFile.array.forEach(record => {
    console.log(`ID: ${record.id}, Name: ${record.name}`)
});

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

document.getElementById('dataContainer').textContent = JSON.stringify(data, null, 2);