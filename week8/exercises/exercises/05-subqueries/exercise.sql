-- Exercise 05: Subqueries
-- Databases: school.db and library.db

.headers on
.mode column

-- 5.1: Students with GPA above the average (school.db)
SELECT first_name, last_name, gpa
FROM students
WHERE gpa > (SELECT AVG(gpa) FROM students);

-- 5.2: Students enrolled in CS50 (use subquery) (school.db)
SELECT first_name, last_name
FROM students
WHERE id IN (
  SELECT student_id
  FROM enrollments
  WHERE course_id = (
    SELECT id
    FROM courses
    WHERE code = 'CS50'
  )
);

-- 5.3: Students NOT enrolled in CS50 (school.db)
SELECT first_name, last_name
FROM students
WHERE id NOT IN (
  SELECT student_id
  FROM enrollments
  WHERE course_id = (
    SELECT id
    FROM courses
    WHERE code = 'CS50'
  )
);

-- 5.4: Courses taught by the highest-paid teacher (school.db)
SELECT title
FROM courses
WHERE teacher_id = (
  SELECT id
  FROM teachers
  WHERE salary = (SELECT MAX(salary) FROM teachers)
);

-- 5.5: Students enrolled in 3 or more courses (subquery in FROM) (school.db)
SELECT student_id
FROM (
  SELECT student_id, COUNT(*) AS course_count
  FROM enrollments
  GROUP BY student_id
)
WHERE course_count >= 3;

-- 5.6: Members who borrowed more than 2 books (library.db)
SELECT member_id
FROM (
  SELECT member_id, COUNT(*) AS borrow_count
  FROM loans
  GROUP BY member_id
)
WHERE borrow_count > 2;

-- 5.7: Books with more pages than average (library.db)
SELECT title, pages
FROM books
WHERE pages > (SELECT AVG(pages) FROM books);

-- 5.8: Students with at least one grade (EXISTS) (school.db)
SELECT first_name, last_name
FROM students s
WHERE EXISTS (
  SELECT 1
  FROM enrollments e
  JOIN grades g ON e.id = g.enrollment_id
  WHERE e.student_id = s.id
);

-- 5.9: Courses with no grades recorded (NOT EXISTS) (school.db)
SELECT title
FROM courses c
WHERE NOT EXISTS (
  SELECT 1
  FROM enrollments e
  JOIN grades g ON e.id = g.enrollment_id
  WHERE e.course_id = c.id
);

-- 5.10 CHALLENGE: Course(s) with the most enrollments (no LIMIT) (school.db)
SELECT title
FROM courses
WHERE id IN (
  SELECT course_id
  FROM (
    SELECT course_id, COUNT(*) AS cnt
    FROM enrollments
    GROUP BY course_id
  )
  WHERE cnt = (
    SELECT MAX(cnt)
    FROM (
      SELECT COUNT(*) AS cnt
      FROM enrollments
      GROUP BY course_id
    )
  )
);

