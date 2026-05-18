SELECT
    strftime('%m-%Y', Date) as mes,
    round(sum(Distance)/1000, 1) AS "distancia caminhada (km)",
    round(sum(MovingTime)/3600, 1) AS "duracao (h)"
FROM activities
WHERE
    strftime('%Y', Date) = '2026'
    AND Type = "Walk"
GROUP BY mes
ORDER BY mes;


SELECT
    round(sum(Distance)/1000, 1) AS "distancia total (km)",
    round(sum(MovingTime)/3600, 1) AS "duracao total (h)"
FROM activities
WHERE
    strftime('%Y', Date) = '2026'
    AND Type = "Walk";
