# Write your MySQL query statement below
with first_login as(
    select player_id, MIN(event_date) AS first_date
    from Activity
    Group By player_id
)
select round(COUNT(DISTINCT a.player_id)/(Select COUNT(DISTINCT player_id)From Activity),2
)As fraction
from Activity a
JOIN first_login f
ON a.player_id = f.player_id
AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);