-- Begin
ALTER TABLE reviews
ADD PRIMARY KEY (review_id);

ALTER TABLE reviews
ADD CONSTRAINT business_id_fk
FOREIGN KEY (business_id)
REFERENCES businesses(business_id)
ON DELETE CASCADE;

ALTER TABLE reviews
ADD CONSTRAINT user_id_fk
FOREIGN KEY (user_id)
REFERENCES users(user_id)
ON DELETE CASCADE;
-- End
