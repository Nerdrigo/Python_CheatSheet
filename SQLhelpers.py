import psycopg2
import sqlalchemy
import os

#Gettin DB information save as environment variables
PG_HOST = os.environ['PG_HOST']  #Host localhost or IP
PG_USR = os.environ['PG_USR']    #User name (role in DB)
PG_PASS = os.environ['PG_PASS']  #User password
PG_DB = os.environ['PG_DB']      #Database name
PG_PORT = os.environ['PG_PORT']  #Port number


def get_postgres_connection():
    '''
    This function connects to a database
    There needs to be an existing connection
    '''
    con = psycopg2.connect(
        "dbname={} user={} password={} host={} port={}".format(
            PG_DB, PG_USR, PG_PASS,
            PG_HOST, PG_PORT
        )
    )
    return con


def create_connection():
    '''
    This function creates a connection to a database
    '''
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(
        PG_USR,
        PG_PASS,
        PG_HOST,
        PG_PORT,
        PG_DB
    )
    return sqlalchemy.create_engine(url)