from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Float
import databases

from setings import settings
from datetime import datetime

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = MetaData()
database.connect()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(10)),
    Column("email", String(20)),
    Column("password", String(128)),
)
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("description", String(255)),
    Column("price", Float),
)
orders = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("order_date", DateTime, default=datetime.now()),
    Column("status", String(50), default="Pending"),
)

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

metadata.create_all(engine)
