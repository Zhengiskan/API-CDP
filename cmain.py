from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from urllib.parse import quote
from config import *
import requests

def connection(c_obj):
    c_dbschema = c_obj.db_name
    c_password = c_obj.db_password
    c_encoded_password = quote(c_password)

    c_engine = create_engine(
        f'postgresql+psycopg2://{c_obj.db_username}:{c_encoded_password}@{c_obj.db_host}:{c_obj.db_port}/{c_dbschema}'
    )

    c_datas = pd.read_sql(c_obj.query, con=c_engine)
    print(c_datas)
    return c_datas


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

payload = {}
formatted_data = {}

url = "https://9eb8d506-3124-42c1-92d2-a8c32732eaf2.mock.pstmn.io/post"
# payload = {
#     "checkin_type": "$checkin_type",
#     "first_name": "$first_name",
#     "last_name": "$last_name",
#     "email": "$email",
#     "birthdate": "$birthdate",
#     "phone_number": "$phone_number",
#     "sx_id": "$sx_id"
# }

for config_obj in config_objects:
    data = connection(config_obj)
    if data is not None:
        data = data.astype(str)
        payload[config_obj.id] = data.to_dict(orient='records')

headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)

print(response.text)
