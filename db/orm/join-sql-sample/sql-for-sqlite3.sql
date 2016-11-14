--Cross join
SELECT *
FROM employee CROSS JOIN department;

--Inner join
SELECT *
FROM employee 
INNER JOIN department ON employee.DepartmentID = department.DepartmentID;

--Left outer join
SELECT *
FROM employee 
LEFT OUTER JOIN department ON employee.DepartmentID = department.DepartmentID;

--Right outer join
SQLite3では対応してない。

--Full outer join
SQLite3では対応してない。

