import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
#con_str = "postgresql://gitpod:postgres:@localhost/milser_pg"
global engine # This allows us to use a global variable called engine
# A "connection string" is basically a string containing all database credentials together.
#connection_string = f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')} host={os.getenv('DB_HOST')}"

total_data = pd.read_csv("../data/raw/AB_NYC_2019.csv")
total_data.head()
#engine = create_engine(connection_string)
#Session = sessionmaker(bind=engine,autocommit=False) 