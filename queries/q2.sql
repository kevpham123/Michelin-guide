-- Begin
DROP MATERIALIZED VIEW IF EXISTS elite_reviews_mv;

CREATE MATERIALIZED VIEW elite_reviews_mv AS
WITH elite_year AS (
    SELECT user_id, TRIM(split_elites) AS unnest_year
    FROM users u
    CROSS JOIN LATERAL UNNEST(elite) AS unnest_elite
    CROSS JOIN LATERAL REGEXP_SPLIT_TO_TABLE(unnest_elite, ',') AS split_elites
), elite_count AS (
    SELECT user_id, COUNT(*)
    FROM elite_year
    WHERE LENGTH(unnest_year) >= 2
    GROUP BY user_id
), elite_users AS (
    SELECT user_id
    FROM users
    WHERE user_id in (SELECT user_id FROM elite_count)
)

SELECT r.review_id, r.user_id, r.business_id, r.stars AS elite_users_rating
FROM reviews r
WHERE r.user_id IN (SELECT user_id FROM elite_users)
AND r.business_id IN (SELECT business_id FROM restaurant_businesses_mv);

CREATE INDEX idx_elite_reviews_mv_business_id ON elite_reviews_mv (business_id);
-- End
