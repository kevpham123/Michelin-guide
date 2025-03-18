-- Begin
DROP TABLE IF EXISTS temp_reviews;
CREATE TABLE temp_reviews (
    review_id VARCHAR(22) PRIMARY KEY,
    user_id VARCHAR(22),
    business_id VARCHAR(22),
    stars INT CHECK (stars >= 0 AND stars <= 5),
    date DATE,
    text TEXT,
    useful INT,
    funny INT,
    cool INT
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    review_id VARCHAR(22) PRIMARY KEY,
    user_id VARCHAR(22) REFERENCES users (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    business_id VARCHAR(22) REFERENCES businesses (business_id) ON DELETE CASCADE ON UPDATE CASCADE,
    stars INT CHECK (stars >= 0 AND stars <= 5),
    date DATE,
    text TEXT,
    useful INT,
    funny INT,
    cool INT
)
-- End
