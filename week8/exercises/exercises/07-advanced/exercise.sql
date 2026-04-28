-- Exercise 07: Advanced SQL
-- Databases: school.db and library.db

.headers on
.mode column

-- 7.1: Create an index on students.gpa, then EXPLAIN QUERY PLAN
CREATE INDEX idx_students_gpa ON students(gpa);

EXPLAIN QUERY PLAN
SELECT *
FROM students
WHERE gpa > 3.0;

-- 7.2: Create view 'enrollment_details', then query for 'A' grades
CREATE VIEW enrollment_details AS
SELECT
    s.first_name,
    s.last_name,
    c.title,
    g.letter_grade
FROM enrollments e
JOIN students s ON e.student_id = s.id
JOIN courses c ON e.course_id = c.id
JOIN grades g ON e.id = g.enrollment_id;

SELECT *
FROM enrollment_details
WHERE letter_grade = 'A';


-- 7.3: Create view 'course_statistics' with count and avg final score
CREATE VIEW course_statistics AS
SELECT
    c.id AS course_id,
    COUNT(g.final) AS total_students,
    AVG(g.final) AS average_score
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
LEFT JOIN grades g ON e.id = g.enrollment_id
GROUP BY c.id;


-- 7.4: Insert a new student (newstudent@school.edu, 2024, NULL gpa)
INSERT INTO students (email, enrollment_year, gpa)
VALUES ('newstudent@school.edu', 2024, NULL);


-- 7.5: Update student id=17 (Quinn Moore) to set gpa = 3.22
UPDATE students
SET gpa = 3.22
WHERE id = 17;

-- 7.6: Preview and then DELETE all grades with letter_grade = 'F'
-- Step 1: SELECT to preview (run this first!)
SELECT *
FROM grades
WHERE letter_grade = 'F';

-- Step 2: DELETE (uncomment when ready)
DELETE FROM grades
WHERE letter_grade = 'F';

-- 7.7: Transaction to enroll student 1 in course 13 + add grade record
BEGIN TRANSACTION;

INSERT INTO enrollments (student_id, course_id)
VALUES (1, 13);

INSERT INTO grades (enrollment_id, letter_grade, final)
VALUES (
    (SELECT id FROM enrollments WHERE student_id = 1 AND course_id = 13),
    'A',
    95
);

COMMIT;


-- 7.8: Transaction: decrease available_copies for book 3, insert loan (library.db)
BEGIN TRANSACTION;

UPDATE books
SET available_copies = available_copies - 1
WHERE id = 3;

INSERT INTO loans (member_id, book_id, loan_date, return_date)
VALUES (1, 3, DATE('now'), NULL);

COMMIT;


-- 7.9: EXPLAIN QUERY PLAN comparison
-- Run both and compare the output:

-- Version A (may not use index well):
EXPLAIN QUERY PLAN
SELECT *
FROM students
WHERE gpa + 0 > 3.0;

-- Version B (index-friendly):
EXPLAIN QUERY PLAN
SELECT *
FROM students
WHERE gpa > 3.0;

-- Your explanation of the difference (as a comment):
-- Version A prevents index usage because it modifies the column (gpa + 0),
-- forcing SQLite to scan the whole table.
--
-- Version B allows index usage because it directly filters on gpa,
-- so SQLite can use idx_students_gpa for faster lookup.


-- 7.10 CHALLENGE: Create compound index for enrollments(student_id, course_id)
CREATE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);
