-- Begin
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id VARCHAR(22) PRIMARY KEY,
    name TEXT NOT NULL,
    review_count INT CHECK (review_count >= 0),
    yelping_since DATE,
    friends TEXT[],
    useful INT CHECK (useful >= 0),
    funny INT CHECK (funny >= 0),
    cool INT CHECK (cool >= 0),
    fans INT CHECK (fans >= 0),
    elite TEXT[],
    average_stars FLOAT CHECK (average_stars >= 0 AND average_stars <= 5),
    compliment_hot INT CHECK (compliment_hot >= 0),
    compliment_more INT CHECK (compliment_more >= 0),
    compliment_profile INT CHECK (compliment_profile >= 0),
    compliment_cute INT CHECK (compliment_cute >= 0),
    compliment_list INT CHECK (compliment_list >= 0),
    compliment_note INT CHECK (compliment_note >= 0),
    compliment_plain INT CHECK (compliment_plain >= 0),
    compliment_cool INT CHECK (compliment_cool >= 0),
    compliment_funny INT CHECK (compliment_funny >= 0),
    compliment_writer INT CHECK (compliment_writer >= 0),
    compliment_photos INT CHECK (compliment_photos >= 0)
);
-- End
