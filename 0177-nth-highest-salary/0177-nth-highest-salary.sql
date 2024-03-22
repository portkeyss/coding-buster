CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  Set n = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select # SELECT can be used to retrieve rows computed without reference to any table
          (select distinct Salary
          from Employee
          order by Salary DESC
          limit n, 1) # limit can take only numerical constants that is why we need to set n = N - 1 and use n here
  );
END