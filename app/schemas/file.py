from typing import Any

from pydantic import BaseModel


class ContentFile(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    contents: Any
