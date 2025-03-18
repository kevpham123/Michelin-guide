-- Begin
DROP TABLE IF EXISTS businesses;

CREATE TABLE businesses (
    business_id VARCHAR(22) PRIMARY KEY,
    name TEXT NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(20),
    postal_code VARCHAR(15),
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT CHECK (stars >= 0 AND stars <= 5),
    review_count INT CHECK(review_count >= 0),
    is_open BOOLEAN,
    attributes JSONB,
    categories TEXT[],
    hours JSONB
);
-- End
