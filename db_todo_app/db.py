from sqlalchemy import (
        Column,
        Integer,
        MetaData,
        String,
        Table,
        create_engine
    )
from databases import Database

Database_URL = "postgresql://root:123@localhost/items_db")

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
