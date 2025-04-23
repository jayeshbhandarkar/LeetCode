SELECT employee_id,
       COALESCE(
           (SELECT department_id FROM Employee e
            WHERE e.employee_id = Employee.employee_id AND e.primary_flag = 'Y'
            LIMIT 1),
           (SELECT department_id FROM Employee e
            WHERE e.employee_id = Employee.employee_id LIMIT 1)
        ) AS department_id
FROM Employee
GROUP BY employee_id;
