from sqlalchemy import create_engine
from urllib.parse import quote
import pandas as pd
from urllib.parse import quote


dbschema = "database_api_cdp"
password = "toto@2021"
encoded_password = quote(password)

engine = create_engine(
    f"mysql+mysqlconnector://toto:{encoded_password}@35.240.144.191:3306/{dbschema}"
)

query = """select * from database_api_cdp.configs where deleted_at is null"""
datas = pd.read_sql(query, con=engine)
