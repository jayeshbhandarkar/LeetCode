Select * from Cinema
Where MOD(id, 2) = 1 AND description != 'Boring'
ORDER BY rating DESC;
