# Write your MySQL query statement below
Select email AS Email from Person Group By email having COUNT(*)>1;