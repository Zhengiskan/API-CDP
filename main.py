import json

from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from urllib.parse import quote
from config import *
import requests


def Post_API(c_obj, source_obj):
    pass


def connection(c_obj):
    c_dbschema = c_obj.db_name
    c_password = c_obj.db_password
    c_encoded_password = quote(c_password)

    c_engine = create_engine(
        f'postgresql+psycopg2://{c_obj.db_username}:{c_encoded_password}@{c_obj.db_host}:{c_obj.db_port}/{c_dbschema}'
    )

    c_datas = pd.read_sql(c_obj.query, con=c_engine)

    url = c_obj.api_host
    headers = json.loads(c_obj.api_headers)
    print("HEAD: ", type(headers))

    for _, c_data in c_datas.iterrows():
        data = {
            "checkin_type": c_data["checkin_type"],
            "first_name": c_data["first_name"],
            "last_name": c_data["last_name"],
            "email": c_data["email"],
            "birthdate": c_data["birthdate"],
            "phone_number": c_data["phone_number"],
            "sx_id": c_data["sx_id"]
        }

        response = requests.post(url, headers=headers, json=data)

        # Print the response status code and content
        print("Response status code:", response.status_code)
        print("Response content:", response.text)


dbschema = "database_api_cdp"
password = "toto@2021"
encoded_password = quote(password)

engine = create_engine(
    f"mysql+mysqlconnector://toto:{encoded_password}@35.240.144.191:3306/{dbschema}"
)

query = """select * from database_api_cdp.configs where deleted_at is null"""
datas = pd.read_sql(query, con=engine)
print(datas)

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

for config_obj in config_objects:
    connection(config_obj)

