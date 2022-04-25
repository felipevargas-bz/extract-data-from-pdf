from typing import Any

from fastapi import HTTPException

from app.crud import extraction_service


def identify_table(table: str) -> Any:
    """Identifies which table is being referenced
       by its name and returns its respective crud service.

    Args:
        table (str): Name of the table that is being referenced.

    Returns:
        Any: returns the controller of the respective table.
    """
    table = table.lower()
    if table == 'extraction':
        return extraction_service
    else:
        raise HTTPException(status_code=400, detail=f"Table {table} dasn't exist")
