from typing import Dict, List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import Extraction as Extraction_model
from app.schemas import Extraction, ExtractionCreate


class ExtractionService:
    """CRUD service for the Extraction model
    """
    @staticmethod
    def create(db: Session, payload: ExtractionCreate) -> Extraction:
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
            extraction = Extraction(**db_obj.__dict__)

            return extraction
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f'An error occurred while creating the Extract Error: {str(e)}')

    @staticmethod
    def get_all(db: Session) -> List[Dict]:
        """Get all extractions

        Args:
            db (Session): Database connection

        Returns:
            List[Extraction]: List of extractions
        """
        try:
            extractions = [db_obj.__dict__ for db_obj in db.query(Extraction_model).all()]
            return extractions
        except Exception as e:
            raise HTTPException(
                status_code=404,
                detail=f'An error occurred while trying to get the Extractions Error: {str(e)}')


extraction_service = ExtractionService()
