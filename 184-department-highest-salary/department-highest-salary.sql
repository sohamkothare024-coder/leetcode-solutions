# Write your MySQL query statement below
SELECT d.name AS Department,e.name AS Employee,e.salary AS Salary 
FROM Employee e
JOIN Department d ON e.departmentId = d.id
Where e.salary = (
    SELECT MAX(salary)
    FROM EMployee e2
    Where e2.departmentId =e.departmentId
);