from langchain_community.utilities import SQLDatabase
#import pymysql
from config import config

def get_database_connection():
    """Establish and return a connection to the database."""
    db_uri = f"mysql+pymysql://{config['db_user']}:{config['db_password']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
    return SQLDatabase.from_uri(db_uri)

db = get_database_connection()
