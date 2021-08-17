# Write your MySQL query statement below
SELECT A.Name AS "Employee"
FROM Employee A JOIN Employee B
ON A.ManagerId = B.ID
WHERE A.Salary > B.Salary