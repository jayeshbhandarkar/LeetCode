Select(
    Select num from Mynumbers
    Group By num
    Having count(num) = 1
    Order By num Desc
    Limit 1
) as num;
