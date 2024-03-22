# Write your MySQL query statement below
delete from Person
where Id in
    (select p1.Id
     from (select * from Person) p1, (select * from Person) p2
     where p1.Email = p2.Email and p1.Id > p2.Id);