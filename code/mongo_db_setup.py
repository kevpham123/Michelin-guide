from SetUp import *

"""
This file is used to initialize the Yelp database in MongoDB using pyMongo
"""

data_retrieval = SetUp()
mongo_db = MongoSetup()
testing = mongo_db.testing

"""
This section is used to initialize the businesses collections for our Yelp database
"""

business_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_business.json'))

# Creating businesses collections then inserting our data into it
businesses = testing.businesses
mongo_db.insert_data(businesses, business_data)

# Delete variable to free up memory
del business_data

"""
This section is used to initialize the user collections for our Yelp database
"""

user_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_user.json'))

# Creating users collections then inserting our data into it
users = testing.users
mongo_db.insert_data(users, user_data)

# Delete variable to free up memory
del user_data

"""
This section is used to initialize the reviews collections for our Yelp database
"""

review_data = list(data_retrieval.retrieve_data('data/yelp_academic_dataset_review.json'))

# Creating reviews collections then inserting our data into it
reviews = testing.reviews
mongo_db.insert_data(reviews, review_data)

# Delete variable to free up memory
del review_data
