WITH T AS
(
SELECT *
    DENSE_RANK() OVER (ORDER BY Salary Desc) AS Rnk
FROM Employee
)
SELECT Salary FROM T WHERE Rnk=n;
