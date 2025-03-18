-- Begin
DROP TABLE IF EXISTS temp_reviews;

CREATE TABLE temp_reviews (
    review_id VARCHAR(22) PRIMARY KEY,
    user_id VARCHAR(22),
    business_id VARCHAR(22),
    stars FLOAT CHECK (stars >= 0 AND stars <= 5),
    useful INT,
    funny INT,
    cool INT,
    text TEXT,
    date DATE
);
-- End
