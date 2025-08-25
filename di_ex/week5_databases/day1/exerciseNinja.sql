SELECT first_name, last_name,birth_date FROM students WHERE id <5 ORDER BY last_name ASC;

SELECT first_name, last_name, birth_date
FROM students
WHERE birth_date = (SELECT MIN(birth_date) FROM students);

SELECT first_name, last_name,birth_date FROM students OFFSET 2 LIMIT 3;