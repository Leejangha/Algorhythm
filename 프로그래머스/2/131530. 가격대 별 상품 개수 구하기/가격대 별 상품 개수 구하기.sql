-- 코드를 입력하세요
SELECT TRUNCATE(PRICE / 10000, 0) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP