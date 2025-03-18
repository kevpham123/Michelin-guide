import json
import pandas as pd
from SetUp import *

postgres = PostgresSetup()
data_retrieval = SetUp()

# Helper function
def format_categories(categories_str):
    if categories_str:
        # Split by commas and strip spaces
        categories_list = [cat.strip() for cat in categories_str.split(',')]
        # Convert to PostgreSQL array format
        return '{' + ','.join(f'"{cat}"' for cat in categories_list) + '}'
    return None

# We first need to initialize the Yelp database
postgres.query("""
DROP DATABASE IF EXISTS Yelp;
""",
db_name='yelp', output=False)
postgres.query("""
CREATE DATABASE Yelp;
""",
db_name='yelp', output=False)

"""
This section is used to initialize the businesses relation for our Yelp database
"""

# Preparing our business data so that we can use \COPY when inserting into businesses relation
business_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_business.json'))
business_data_df = pd.DataFrame(business_data)
business_data_df['attributes'] = business_data_df['attributes'].apply(json.dumps)
business_data_df['hours'] = business_data_df['hours'].apply(json.dumps)
business_data_df['categories'] = business_data_df['categories'].apply(format_categories)
business_data_df.to_csv('data/businesses.csv', index=False)

# Creating our businesses relation with our constraints
postgres.query('queries/add_drop_businesses.sql', db_name='yelp', file=True, explain=False, output=False)

# Inserting our data into the businesses relation
postgres.insert_data('data/businesses.csv', db_name='yelp', relation_name='businesses')

"""
This section is used to initialize the users relation for our Yelp database
"""

# Preparing our user data so that we can use \COPY when inserting into user relation
user_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_user.json'))
user_data_df = pd.DataFrame(user_data)
user_data_df['friends'] = user_data_df['friends'].apply(format_categories)
user_data_df['elite'] = user_data_df['elite'].apply(format_categories)
user_data_df.to_csv('data/users.csv', index=False)

# Creating our users relation with our constraints
postgres.query('queries/add_drop_users.sql', db_name='yelp', file=True, explain=False, output=False)

# Inserting our data in the users relation
postgres.insert_data('data/users.csv', db_name='yelp', relation_name='users')

"""
This section is used to initialize the reviews relation for our Yelp database
To complete the Postgres database setup, we need to finish a couple more steps because our data is incomplete and inconsistent
There exists some reviews for businesses/users that does not exist in both businesses or users relation
This section will filter out those reviews and only insert reviews for businesses and users that exists in our database
This section is expected to take a couple minutes to finish
"""

# Preparing our review data so that we can use \COPY when inserting into reviews relation
review_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_review.json'))
review_data_df = pd.DataFrame(review_data)
review_data_df.to_csv('data/reviews.csv', index=False)

# Creating our review_temp relation with no constraints
postgres.query('queries/add_drop_temp_reviews.sql', db_name='yelp', file=True, explain=False, output=False)

# Inserting reviews data into temp_reviews relation
postgres.insert_data('data/reviews.csv', db_name='yelp', relation_name='temp_reviews')

# Now insert the query results from temp_reviews into the reviews relation
postgres.query('queries/add_drop_reviews.sql', db_name='yelp', file=True, explain=False, output=False)

# Finally, time to create an index on review_id and add foregin key constraints for businesses and users relation
postgres.query('queries/add_reviews_constraints.sql', db_name='yelp', file=True, explain=False, output=False)

# Removing the temporary relation from the database
postgres.query("""
DROP TABLE IF EXISTS temp_reviews;
""",
db_name='yelp', output=False)
