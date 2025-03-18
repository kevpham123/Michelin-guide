import os
import json
import pymongo
import psycopg as psycopg
import pandas as pd
from dotenv import load_dotenv

class SetUp:
    def __init__(self):
        pass

    def retrieve_data(self, file_address):
        toReturn = []
        with open(file_address, encoding="utf8") as file:
            for line in file:
                toReturn.append(json.loads(line))
        return toReturn

class PostgresSetup(SetUp):
    def __init__(self):
        super().__init__()

    def insert_data(self, file_name: str, db_name: str, relation_name: str):
        load_dotenv()
        conn = psycopg.connect(f"dbname={db_name} user={os.getenv('USER_NAME')} password={os.getenv('PSQL_PASSWORD')}",
                                autocommit=True)
        cur = conn.cursor()
        with conn.cursor() as cur:
            with open(file_name, encoding="utf8") as file:
                with cur.copy(f"COPY {relation_name} FROM STDIN WITH CSV HEADER") as copy:
                    for line in file:
                        copy.write(line)
        cur.close()
        conn.close()


    def query(self, query, db_name: str, file=False, explain=False, output=True):
        load_dotenv()
        conn = psycopg.connect(f"dbname={db_name} user={os.getenv('USER_NAME')} password={os.getenv('PSQL_PASSWORD')}", 
                               autocommit=True)
        cur = conn.cursor()

        row = None
        col = None

        if file == False:
            if output == False:
                cur.execute(query)
                cur.close()
                conn.close()
                return
            cur.execute(query)
            row = cur.fetchall()
            col = [cur.description[i][0] for i in range(len(cur.description))]
        else:
            with open(query) as file:
                sql_script = file.read()
            if output == False:
                cur.execute(sql_script)
                cur.close()
                conn.close()
                return
            cur.execute(sql_script)
            row = cur.fetchall()
            col = [cur.description[i][0] for i in range(len(cur.description))]

        cur.close()
        conn.close()
        if explain == False:
            return pd.DataFrame(row, columns=col)
        else:
            return row

class MongoSetup(SetUp):
    def __init__(self):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.testing = client.testing
        super().__init__()
    
    def insert_data(self):
        pass

