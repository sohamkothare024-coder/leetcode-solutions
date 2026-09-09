# Write your MySQL query statement below
SELECT 
    p.firstName AS FirstName,
    p.lastName AS LastName,
    a.city AS City,
    a.state AS State
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;