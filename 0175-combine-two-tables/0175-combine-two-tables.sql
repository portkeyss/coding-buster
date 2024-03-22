# Write your MySQL query statement below
select FirstName, LastName, City, State
from Person p
Left join Address a on p.PersonId = a.PersonId;