CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        From Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
  );
END
