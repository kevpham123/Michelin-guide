from SetUp import *

"""
This file is used to initialize the Yelp database in MongoDB using pyMongo
"""

data_retrieval = SetUp()
mongo_DB = MongoSetup()
testing = mongo_DB.testing

"""
This section is used to initialize the businesses collections for our Yelp database
"""

business_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_business.json'))

businesses = testing.businesses
businesses.insert_many(business_data)

"""
This section is used to initialize the user collections for our Yelp database
"""

user_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_user.json'))

users = testing.users
users.insert_many(user_data)

"""
This section is used to initialize the reviews collections for our Yelp database
"""

review_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_review.json'))

reviews = testing.reviews
reviews.insert_many(review_data)
