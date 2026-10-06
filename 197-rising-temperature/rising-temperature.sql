# Write your MySQL query statement below
Select w1.id From Weather w1
Join Weather w2 on w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;