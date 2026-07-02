CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);

INSERT INTO students VALUES
(1,'Asha',20),
(2,'Rahul',21),
(3,'Fidha',20);

SELECT * FROM students;

-- UPDATE
UPDATE students
SET age = 22
WHERE id = 1;

SELECT * FROM students;

-- DELETE
DELETE FROM students
WHERE id = 3;

SELECT * FROM students;

-- WHERE
SELECT * FROM students
WHERE age = 21;

INSERT INTO students VALUES
(4,'Anu',19)
(5,'Arun',22)

SELECT * FROM students
ORDER BY age;

SELECT * FROM students
ORDER BY age DESC;

SELECT * FROM students
LIMIT 3;

SELECT * FROM students
ORDER BY age
LIMIT 2;
