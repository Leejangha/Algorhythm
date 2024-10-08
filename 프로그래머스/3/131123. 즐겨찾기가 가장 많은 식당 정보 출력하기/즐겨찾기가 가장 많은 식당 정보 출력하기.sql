-- 코드를 입력하세요
SELECT R.FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO AS R
INNER JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) AS M_FAVORITES FROM REST_INFO GROUP BY FOOD_TYPE) AS I
    ON R.FOOD_TYPE = I.FOOD_TYPE AND R.FAVORITES = I.M_FAVORITES
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC