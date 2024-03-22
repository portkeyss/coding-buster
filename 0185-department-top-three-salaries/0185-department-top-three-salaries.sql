# Write your MySQL query statement below
select d.Name Department, e1.name Employee, e1.Salary
from Employee e1, Department d
where e1.DepartmentId = d.Id 
 and (select count(distinct e2.Salary)
          from Employee e2
           where e2.DepartmentId = e1.DepartmentId and e2.Salary > e1.Salary) < 3