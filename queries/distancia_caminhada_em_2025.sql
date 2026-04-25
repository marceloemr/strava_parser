SELECT
    strftime('%m-%Y', Date) as mes,
    round(sum(Distance)/1000, 1) AS "distancia caminhada"
FROM activities
WHERE
    strftime('%Y', Date) = '2025'
    AND Type = "Walk"
GROUP BY mes
ORDER BY mes;


SELECT round(sum(Distance)/1000, 1) AS "Total"
FROM activities
WHERE
    strftime('%Y', Date) = '2025'
    AND Type = "Walk";
