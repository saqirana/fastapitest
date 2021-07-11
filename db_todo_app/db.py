from sqlalchemy import (
        Column,
        Integer,
        MetaData,
        String,
        Table,
        create_engine
    )
from databases import Database
from environs import Env

env = Env()
env.read_env()
db = env("DATABASE")
user = env("USER")
password = env("PASSWORD")
host = env("HOST")
dbname = env("DBNAME")

Database_URL = "{0}://{1}:{2}@{3}/{4}".format(db, user, password, host, dbname)

engine = create_engine(Database_URL)
metadata = MetaData()

Items = Table(
        "items",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("title", String(100)),
        Column("description", String(100))
)


database = Database(Database_URL)
