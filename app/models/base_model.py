from datetime import datetime

from sqlalchemy import Column, DateTime, Integer

from app.config import Base


class BaseModel(Base):
    """
    Base class for all models
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """
        Initialize base model
        """
        super().__init__(*args, **kwargs)
