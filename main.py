from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from urllib.parse import quote

dbschema = 'database_api_cdp'
password = 'toto@2021'
encoded_password = quote(password)

engine = create_engine(
    f'mysql+mysqlconnector://toto:{encoded_password}@35.240.144.191:3306/{dbschema}'
)

# query = "select * from disaster.waterlevel_station ws join disaster.mapped wm on ws.id = wm.source;"select * from
# disaster.waterlevel_station ws left join disaster.mapped wm on ws.id = wm.source

query = """select * from database_api_cdp.configs"""
data = pd.read_sql(query, con=engine)

print(data)