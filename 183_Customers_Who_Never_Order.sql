Select name as Customers 
From Customers
Where id NOT IN (Select customerId From Orders);
