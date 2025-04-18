from urllib.parse import quote
import pandas as pd
import requests

def connection(c_obj):
    c_dbschema = c_obj.db_name
    c_password = c_obj.db_password
    c_encoded_password = quote(c_password)

    c_engine = create_engine(
    )

    c_datas = pd.read_sql(c_obj.query, con=c_engine)
    print(c_datas)
    return c_datas


dbschema = "xxxxx"
password = "xxxxx"
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
    )
    data = connection(config_obj)


