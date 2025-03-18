# Michelin Guide

---

## Overview

This project is an adaptation of the final project from Data 101 at UC Berkeley. Its primary goal is to explore the strengths and weaknesses of SQL and NoSQL databases and to understand the conditions under which one is more suitable than the other. For this project, I utilized the publicly available [Yelp dataset](https://business.yelp.com/data/resources/open-dataset/), PostgreSQL and MongoDB.

---

## Set Up

To get started, you'll need to download the [Yelp dataset](https://business.yelp.com/data/resources/open-dataset/), extract the _.tar_ file, and place the business, review, and users json file into the data directory. In addition, you will also need to create a .env file to store the login information for Postgres. The file should contain a *USER_NAME* and *PASSWORD* variable for Postgres and *MONGO_CLIENT* for MongoDB. The final step is to run either ***mongo_db_setup.ipynb*** and ***postgres_db_setup.ipynb*** or run ***mongo_db_setup.py*** and ***postgres_db_setup.py***. Running either will produce the same Yelp Database but the latter will initalize significantly quicker. The Yelp database after initializing will contain relations businesses, reviews, and users.

A diagram of the Yelp database is shown below. This diagram was created using [dbdiagram](https://dbdiagram.io/home).

<iframe
    width="100%"
    height="600"
    src='https://dbdiagram.io/e/67d9ed8175d75cc84496a469/67d9ee7375d75cc84496b452'> 
</iframe>

---

## Objectives

This goal of this project is to learn how to perform ELT, clean data so that it fits our database constraints, and transform our data to learn something informative about it. With that said, I decided to create a Michelin guide based off elite users. According to Yelp, elite users are those that are "active and influential members, recognized for their valuable contributions to the Yelp community, including high-quality reviews, photos, and engagement". We will based our Michelin guide based off these users reviews and star ratings.

---

## Repository Structure

```
├── README.md                   # Project documentation
├── code/                       # Place to put code, scripts, etc.
    ├── __init__.py             # Used to make directory a module
    ├── mongo_db_queries.ipynb  # Run file to run MongoDB queries
    ├── mongo_db_setup.ipynb    # Run file to initialize Yelp in MongoDB
    ├── mongo_db_setup.py       # Run file to initialize Yelp in MongoDB
    ├── postgres_queries.ipynb  # Run file to run PostgreSQL queries
    ├── postgres_setup.ipynb    # Run file to initialize Yelp in PostgreSQL
    ├── postgres_setup.py       # Run file to initialize Yelp in PostgreSQL
    ├── SetUp.py                # The SetUp class is used to initialize Yelp in PostgreSQL and MongoDB
├── data/                       # Data directory (excluded from git)
├── queries/                    # Place to put SQL queries
├── .env                        # Env file to place PostgreSQL user_name, password, and MongoDB client (excluded from git)
```
