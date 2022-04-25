from typing import Any, Dict, List

from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models import Extraction as Extraction_model
from app.schemas import ExtractionCreate, ExtractionResponse


class ExtractionService:
    """CRUD service for the Extraction model"""

    @staticmethod
    def create(db: Session, payload: ExtractionCreate) -> List[Any]:
        """Create new extraction

        Args:
            db (Session): Database connection
            payload (ExtractionCreate): Extract data to store the database.

        Returns:
            Extraction: Extract data stored in the database.
        """
        try:
            db_obj = Extraction_model(**payload.dict())
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            extraction = ExtractionCreate(**db_obj.__dict__)

            return [[True, db_obj.id], extraction.dict()]
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"An error occurred while creating the Extract Error: {str(e)}",
            )

    @staticmethod
    def get_all(db: Session) -> List[Dict]:
        """Get all extractions

        Args:
            db (Session): Database connection

        Returns:
            List[Extraction]: List of extractions
        """
        try:
            extractions = []
            for obj in db.query(Extraction_model).order_by(desc(Extraction_model.id)):
                extraction = ExtractionResponse()
                setattr(extraction, "id", obj.id)
                setattr(extraction, "Vendor_Name", obj.Vendor_Name)
                setattr(extraction, "Fiscal_Number", obj.Fiscal_Number)
                setattr(extraction, "Contract", obj.Contract)
                setattr(extraction, "Start_Date", obj.Start_Date)
                setattr(extraction, "End_date", obj.End_date)
                setattr(extraction, "Comments", obj.Comments)
                setattr(extraction, "Doc_Path", obj.Doc_Path)
                extractions.append(extraction.__dict__)
            return extractions
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f"An error occurred while trying to get the Extractions Error: {str(e)}",
            )


extraction_service = ExtractionService()
