from sqlalchemy import Column, String, Text

from .base_model import BaseModel


class Extraction(BaseModel):

    __tablename__ = "extractions"
    Vendor_Name = Column(String(128), nullable=False)
    Fiscal_Number = Column(String(128), nullable=False)
    Contract = Column(String(128), nullable=False)
    Start_Date = Column(String(15), nullable=False)
    End_date = Column(String(15), nullable=False)
    Comments = Column(Text, nullable=False)
    Doc_Path = Column(String(200), nullable=False)
