from typing import Optional

from pydantic import BaseModel


class ExtractionBase(BaseModel):
    Vendor_Name: str
    Fiscal_Number: str
    Contract: str
    Start_Date: str
    End_date: str
    Comments: str
    Doc_Path: str


class ExtractionCreate(ExtractionBase):
    pass


class Extraction(ExtractionBase):
    id: int

    class Config:
        orm_mode = True


class ExtractionPayload(BaseModel):
    Vendor_Name: Optional[str] = None
    Fiscal_Number: Optional[str] = None
    Contract: Optional[str] = None
    Start_Date: Optional[str] = None
    End_date: Optional[str] = None
    Comments: Optional[str] = None
    Doc_Path: Optional[str] = None
