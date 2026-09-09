CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE varN INT;
  
  -- Calculate offset: to get the N-th item, skip (N-1) items
  SET varN = N - 1;
  
  RETURN (
      SELECT DISTINCT Salary
      FROM Employee
      ORDER BY Salary DESC
      LIMIT varN, 1
  );
END