SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary FROM (
    SELECT e1.Name, e1.Salary, e2.DepartmentId FROM Employee AS e1 WHERE 3 > (
        SELECT count(DISTINCT e2.Name) FROM Employee e2 WHERE e2.Salary > e2.Salary
    )
) AS e JOIN Department AS d ON e.DepartmentId = d.Id;
