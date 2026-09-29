from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    insert,
    inspect,
    text,
)
from sqlalchemy.pool import StaticPool

engine = create_engine(
    "sqlite:///:memory:",
    echo=True,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
metadata_obj = MetaData()

def insert_row_into_table(rows, table, engine=engine):
    for row in rows:
        stmt = insert(table).values(**row)
        with engine.begin() as conn:
            conn.execute(stmt)

table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)

metadata_obj.create_all(engine)

rows = [
    {"id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]

insert_row_into_table(rows, receipts)


inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("receipts")]
table_description = "Columns:\n" + "\n".join([f"- {name}: {type_}" for name, type_ in columns_info])
print(table_description)