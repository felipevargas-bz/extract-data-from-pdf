from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.config import SessionLocal
from app.crud import extraction_service
from app.schemas import ContentFile, ExtractionCreate
from app.utils import (check_filePDF, extract_data_pdf, extract_pdf_text,
                       identify_table, list_files, remove_file, save_file)

router = APIRouter()


# Dependency
def get_db():
    """Get connection to database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/db_data",
    responses={
        200: {"Success": "Extraction data was successfully retrieved"},
        400: {
            "Bad Request": "The request could not be understood by the server due to malformed syntax"
        },
        404: {
            "Not Found": "The requested resource could not be found but may be available again in the future"
        },
    },
    response_class=JSONResponse,
    response_model=List[Dict[str, str]],
)
def get_data_by_table(table_name: str, db: Session = Depends(get_db)):
    """_summary_

    Args:
        table_name (str): Name of the table from which the information is be
                          be extracted.
        db (Session, optional): Database connection. Defaults to Depends(get_db).

    Returns:
        List[data by table_name]: All the data stored in the database stored in the database,
                                  respective to the table that was passed in the table_name variable.
    """
    service = identify_table(table_name)
    response = service.get_all(db=db)
    if response:
        return JSONResponse(content=response, status_code=200)
    else:
        raise HTTPException(status_code=404, detail={"message": "No data found"})


@router.post(
    "/extract",
    responses={
        201: {"Created": "Extraction data was successfully created"},
        400: {
            "Bad Request": "The request could not be understood by the server due to malformed syntax"
        },
        500: {
            "Internal Server Error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
        },
    },
    response_class=JSONResponse,
    response_model=ExtractionCreate,
)
def create_extraction_by_path(*, path: str, db: Session = Depends(get_db)):
    """It extracts the data from the pdf whose path was passed as a parameter, then calls the
       create function to store that data in the database.


    Args:
        path (str): path of the document to which the data extraction process will be carried out.
        db (Session, optional): Database connection. Defaults to Depends(get_db ).

    Returns:
        Extraction: Returns the data extracted from the pdfs that were later saved in the database.
    """
    text = extract_pdf_text(path)
    if text and len(text) > 1:
        extractions: List[ContentFile] = []
        for i in range(len(text)):
            extraction_page: ExtractionCreate = ExtractionCreate(
                **extract_data_pdf(text[i], path)
            )
            extractions.append(
                extraction_service.create(db=db, payload=extraction_page)
            )
            return JSONResponse(status_code=201, content=extractions)
    elif text and len(text) == 1:
        extraction: ExtractionCreate = ExtractionCreate(
            **extract_data_pdf(text[0], path)
        )
        return JSONResponse(
            status_code=201,
            content=extraction_service.create(db=db, payload=extraction),
        )
    else:
        raise HTTPException(status_code=400, detail="Bad request")


@router.post(
    "/upload-pdf",
    responses={
        201: {"Uploaded": "PDF was successfully uploaded"},
        400: {
            "Bad Request": "The request could not be understood by the server due to malformed syntax"
        },
        500: {
            "Internal Server Error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
        },
    },
    response_class=JSONResponse,
    response_model=Dict[str, str],
)
def upload_pdf(contents_pdf: ContentFile = Depends(check_filePDF)):
    """Save the file passed in the Body in the container that is running the application, in the path
       /usr/src/app/files/pdf.

    Args:
        file (UploadFile, optional): PDF file passed in the Body. Depends(check_filePDF).
    """

    file_path = save_file(contents_pdf.name, contents_pdf.contents)
    return JSONResponse(
        status_code=201,
        content={"message": f"File uploaded successfully to {file_path}"},
    )


@router.get(
    "/paths",
    responses={
        200: {"Success": "List of files was successfully retrieved"},
        400: {
            "Bad Request": "The request could not be understood by the server due to malformed syntax"
        },
        500: {
            "Internal Server Error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
        },
    },
    response_class=JSONResponse,
    response_model=List[str],
)
def get_paths(file_name: Optional[str] = None):
    """Get all the paths of the uploaded documents, if and only if file_name == None, otherwise get the
       path of the file whose name is the value of file_name.

    Args:
        file_name (Optional[str], optional): Name of the file to which we are going to obtain its path. Defaults to None.

    Returns:
        List[Dict[str, str]]: List of paths stored on the server.
    """
    return JSONResponse(status_code=200, content=list_files(file_name))


@router.delete(
    "/delete-file",
    responses={
        202: {"Deleted": "File was successfully deleted"},
        400: {
            "Bad Request": "The request could not be understood by the server due to malformed syntax"
        },
        500: {
            "Internal Server Error": "The server encountered an unexpected condition which prevented it from fulfilling the request"
        },
    },
    response_class=JSONResponse,
    response_model=Dict[str, Any],
)
def delete_file(file_name: Optional[str] = None):
    """Deletes a document stored on the server by name.

    Args:
        file_name (Optional[str], optional): Name of the file to delete. Defaults to None.

    Returns:
        Dict[str, str]: Message indicating if the file was deleted or not.
    """

    return JSONResponse(status_code=202, content=remove_file(file_name))
