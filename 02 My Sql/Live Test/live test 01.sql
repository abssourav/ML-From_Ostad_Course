CREATE SCHEMA Google;
use Google;

-- have to create table
-- have insert data into table

SELECT department, AVG(salary) AS average_salary
FROM Google_salaries
GROUP BY department;