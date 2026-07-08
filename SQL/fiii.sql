-- ===========================
-- CREATE TABLE
-- ===========================

CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);

-- ===========================
-- INSERT DATA
-- ===========================

INSERT INTO students VALUES
(1,'Asha',20),
(2,'Rahul',21),
(3,'Fidha',20),
(4,'Anu',19),
(5,'Arun',22);

-- ===========================
-- DISPLAY ALL STUDENTS
-- ===========================

SELECT * FROM students;

-- ===========================
-- UPDATE
-- ===========================

UPDATE students
SET age = 22
WHERE id = 1;

UPDATE students
SET name = 'Fidha Nasrin'
WHERE id = 3;

SELECT * FROM students;

-- ===========================
-- DELETE
-- ===========================

DELETE FROM students
WHERE id = 5;

SELECT * FROM students;

-- ===========================
-- WHERE
-- ===========================

SELECT * FROM students
WHERE age = 21;

-- ===========================
-- ORDER BY
-- ===========================

SELECT * FROM students
ORDER BY age;

SELECT * FROM students
ORDER BY age DESC;

SELECT * FROM students
ORDER BY name;

-- ===========================
-- LIMIT
-- ===========================

SELECT * FROM students
LIMIT 3;

SELECT * FROM students
ORDER BY age
LIMIT 2;

-- ===========================
-- IN
-- ===========================

SELECT * FROM students
WHERE id IN (1,3);

-- ===========================
-- BETWEEN
-- ===========================

SELECT * FROM students
WHERE age BETWEEN 20 AND 22;

-- ===========================
-- ALTER TABLE
-- ===========================

ALTER TABLE students
ADD COLUMN department VARCHAR(50);

UPDATE students
SET department = 'AI & DS'
WHERE id = 1;

UPDATE students
SET department = 'CSE'
WHERE id = 2;

UPDATE students
SET department = 'AI & DS'
WHERE id = 3;

UPDATE students
SET department = 'ECE'
WHERE id = 4;

SELECT * FROM students;

-- ===========================
-- COUNT
-- ===========================

SELECT COUNT(*) AS Total_Students
FROM students;

-- ===========================
-- DISTINCT
-- ===========================

SELECT DISTINCT department
FROM students;

-- ===========================
-- LIKE
-- ===========================

SELECT * FROM students
WHERE name LIKE 'F%';

SELECT * FROM students
WHERE name LIKE '%a';

SELECT * FROM students
WHERE name LIKE '%id%';

-- ===========================
-- CREATE COURSES TABLE
-- ===========================

CREATE TABLE courses (
    course_id INT,
    course_name VARCHAR(50),
    student_id INT
);

-- ===========================
-- INSERT COURSES
-- ===========================

INSERT INTO courses VALUES
(101,'Python',1),
(102,'SQL',2),
(103,'Power BI',1),
(104,'Web Development',4);

-- ===========================
-- DISPLAY COURSES
-- ===========================

SELECT * FROM courses;

-- ===========================
-- INNER JOIN
-- ===========================

SELECT students.id,
students.name,
courses.course_name
FROM students
INNER JOIN courses
ON students.id = courses.student_id;

-- ===========================
-- LEFT JOIN
-- ===========================

SELECT students.id,
students.name,
courses.course_name
FROM students
LEFT JOIN courses
ON students.id = courses.student_id;

-- ===========================
-- RIGHT JOIN
-- (Works only in databases that support RIGHT JOIN)
-- ===========================

SELECT students.id,
students.name,
courses.course_name
FROM students
RIGHT JOIN courses
ON students.id = courses.student_id;