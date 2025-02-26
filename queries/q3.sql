-- Begin
DROP MATERIALIZED VIEW IF EXISTS michelin_guide_mv;

CREATE MATERIALIZED VIEW michelin_guide_mv AS
WITH elite_users_ratings AS (
    SELECT business_id,
    AVG(elite_users_rating) AS elite_users_avg_rating,
    COUNT(*) AS total_elite_reviews
    FROM elite_reviews_mv
    GROUP BY business_id
), elite_businesses_ratings AS (
    SELECT name AS business_name, business_id,
    total_elite_reviews,
    ROUND(elite_users_avg_rating, 3) AS elite_users_avg_rating,
    stars AS all_users_avg_rating
    FROM restaurant_businesses_mv rbmv
    NATURAL JOIN elite_users_ratings eur
)

SELECT *,
CASE 
    WHEN elite_users_avg_rating >= 4.5 AND elite_users_avg_rating <= 5 THEN 3
    WHEN elite_users_avg_rating >= 4 AND elite_users_avg_rating < 4.5 THEN 2
    ELSE 1 END AS Michelin_star
FROM elite_businesses_ratings
WHERE total_elite_reviews >= 100 AND all_users_avg_rating >= 3.8
ORDER BY elite_users_avg_rating DESC;
-- End
