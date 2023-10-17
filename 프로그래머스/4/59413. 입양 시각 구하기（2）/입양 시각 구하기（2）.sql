-- 코드를 입력하세요
WITH RECURSIVE cte_count 
AS ( 
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 AS num
    FROM cte_count
    WHERE HOUR < 23 
)

SELECT cte_count.HOUR, IFNULL(COUNT, 0) AS COUNT
FROM cte_count
LEFT JOIN (SELECT HOUR(O.DATETIME) AS HOUR, COUNT(*) AS COUNT FROM ANIMAL_OUTS AS O GROUP BY HOUR) AS A
    ON cte_count.HOUR = A.HOUR
