SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary FROM (
    SELECT Name, max(Salary), DepartmentId FROM Employee GROUP BY DepartmentId
) AS e JOIN Department AS d ON e.DepartmentId = d.Id;
