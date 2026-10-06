# Write your MySQL query statement below
Select d.name As Department,e.name As Employee,e.salary As Salary 
From Employee e
JOIN Department d ON e.departmentID=d.id
where(
    Select COUNT(DISTINCT e2.salary)
    from Employee e2
    where e2.departmentId =e.departmentId AND e2.salary > e.salary
)<3;