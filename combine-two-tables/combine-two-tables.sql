# Write your MySQL query statement below
SELECT A.FirstName, A.LastName, B.City, B.State
FROM Person A LEFT OUTER JOIN Address B
ON A.PersonId = B.PersonId