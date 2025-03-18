# Michelin Guide

---

## Overview

This project is an adaptation of the final project from Data 101 at UC Berkeley. Its primary goal is to explore the strengths and weaknesses of SQL and NoSQL databases and to understand the conditions under which one is more suitable than the other. For this project, I utilized the publicly available [Yelp dataset](https://business.yelp.com/data/resources/open-dataset/), PostgreSQL and MongoDB.

---

## Set Up

To get started, you'll need to download the [Yelp dataset](https://business.yelp.com/data/resources/open-dataset/) and place the business, review, and users json file into the data directory. In addition, you will also need to create a .env file to store the login information for Postgres. The file should contain a *USER_NAME* and *PASSWORD* variable for Postgres. The final step is to run ***mongo-db-stepup.ipynb*** and ***postgres-db-stepup.ipynb***. These will then make a MongoDB and PostgreSQL database with the relation businesses, reviews, and users. A diagram of this database is shown below. This diagram was created using [dbdiagram](https://dbdiagram.io/home).

---

## Repository Structure

```
├── README.md           # Project documentation
├── code/               # Place to put code, scripts, etc.
├── data/               # Data directory (excluded from git)
├── queries/            # Place to put SQL queries
├── .env                # Env file to place postgres user and password
```
