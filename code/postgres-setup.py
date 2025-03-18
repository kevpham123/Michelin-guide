import pandas as pd
import json
from setup import *

postgres = PostgresSetup()
data_retrieval = Setup()

# # We need to first initialize the Yelp Database
# postgres.query("""
# DROP DATABASE IF EXISTS Yelp;
# """,
# 'postgres',output=False)
# postgres.query("""
# CREATE DATABASE Yelp;
# """,
# 'postgres',output=False)

"""
This section is to make the businesses relation for our Yelp Database
"""

# Preparing our business data so that we can use \COPY when inserting into businesses relation
business_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_business.json'))
business_data_df = pd.DataFrame(business_data)
business_data_df['attributes'] = business_data_df['attributes'].apply(json.dumps)
business_data_df['hours'] = business_data_df['hours'].apply(json.dumps)
def format_categories(categories_str):
    if categories_str:
        # Split by commas and strip spaces
        categories_list = [cat.strip() for cat in categories_str.split(',')]
        # Convert to PostgreSQL array format
        return '{' + ','.join(f'"{cat}"' for cat in categories_list) + '}'
    return None
business_data_df['categories'] = business_data_df['categories'].apply(format_categories)
business_data_df.to_csv('data/businesses.csv', index=False)

# Creating our businesses relation with our constraints
postgres.query('queries/add_drop_businesses.sql', db_name='postgres', file=True, explain=False, output=False)

# Inserting our data into the businesses relation
postgres.insert_data('data/businesses.csv', 'postgres', 'businesses')

"""
This section is to make the users relation for our Yelp Database
"""

# Preparing our user data so that we can use \COPY when inserting into user relation
user_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_user.json'))
user_data_df = pd.DataFrame(user_data)

# Creating our users relation with our constraints
postgres.query('queries/add_drop_users.sql', db_name='postgres', file=True, explain=False, output=False)

# Inserting our data in the users relation
postgres.insert_data('data/yelp_academic_dataset_user.json', 'postgres', 'users')

"""
This section is to make the reviews relation for our Yelp Database
This section will take a couple more steps to finish because our data is incomplete and inconsistent
There exists reviews for businesses that do not exist in our businesses relation
This section will filter out those reviews and only insert reviews for businesses that exist in our businesses relation
This section is expected to take a couple minutes to finish
"""

# Preparing our review data so that we can use \COPY when inserting into reviews relation
review_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_review.json'))
review_data_df = pd.DataFrame(review_data)
