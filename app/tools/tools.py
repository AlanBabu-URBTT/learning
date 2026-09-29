from smolagents import tool
from sqlalchemy import text
from app.db.db import engine

@tool
def sql_engine(query: str)->str:
    """
    Runs read-only SELECT queries on the table and returns their rows as a string.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    statement = query.lstrip().split(None, 1)
    if not statement or statement[0].upper() != "SELECT":
        raise ValueError("Only SELECT queries are allowed")

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return "\n".join(str(row) for row in result)