-- Begin
DROP MATERIALIZED VIEW IF EXISTS restaurant_businesses_mv;

CREATE MATERIALIZED VIEW restaurant_businesses_mv AS
WITH businesses_categories AS (
    SELECT business_id, name, TRIM(split_category) AS category
    FROM businesses b
    CROSS JOIN LATERAL UNNEST(categories) AS unnest_category
    CROSS JOIN LATERAL REGEXP_SPLIT_TO_TABLE(unnest_category, ',') AS split_category
), restaurant_businesses AS (
    SELECT DISTINCT business_id
    FROM businesses_categories
    WHERE category = 'Restaurants' OR category = 'Food'
)

SELECT business_id, name, stars
FROM businesses
WHERE business_id IN (SELECT business_id FROM restaurant_businesses);
-- End
