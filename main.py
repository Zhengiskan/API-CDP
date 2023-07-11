from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from urllib.parse import quote
from config import *


def connection(c_obj):
    c_dbschema = c_obj.name
    c_password = c_obj.db_password
    c_encoded_password = quote(c_password)

    c_engine = create_engine(
        f'mysql+mysqlconnector://{c_obj.db_username}:{encoded_password}{c_obj.db_host}:{c_obj.db_port}/{dbschema}'
    )

    c_datas = pd.read_sql(c_obj.query, con=engine)

    return c_datas

dbschema = "database_api_cdp"
password = "toto@2021"
encoded_password = quote(password)

engine = create_engine(
    f"mysql+mysqlconnector://toto:{encoded_password}@35.240.144.191:3306/{dbschema}"
)

query = """select * from database_api_cdp.configs where deleted_at is null"""
datas = pd.read_sql(query, con=engine)

config_objects = []
for _, row in datas.iterrows():
    config_obj = Config(
        id=row['id'],
        name=row['name'],
        query=row['query'],
        db_host=row['db_host'],
        db_username=row['db_username'],
        db_password=row['db_password'],
        db_name=row['db_name'],
        db_port=row['db_port'],
        api_type=row['api_type'],
        api_host=row['api_host'],
        api_method=row['api_method'],
        api_headers=row['api_headers'],
        api_body=row['api_body'],
        event_name=row['event_name'],
        created_at=row['created_at'],
        updated_at=row['updated_at'],
        deleted_at=row['deleted_at']
    )
    config_objects.append(config_obj)

<<<<<<< HEAD
for config_obj in config_objects:
    connection(config_obj)
=======
# hi
>>>>>>> d06e67c0aec1386ea449039cabe296b3c89acaca
