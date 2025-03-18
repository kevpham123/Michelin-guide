-- Begin
DROP TABLE IF EXISTS reviews;

CREATE TABLE reviews AS ( 
    SELECT *
    from temp_reviews
    WHERE user_id IN (SELECT user_id FROM users) AND
        business_id IN (SELECT business_id FROM businesses)
);
-- End
