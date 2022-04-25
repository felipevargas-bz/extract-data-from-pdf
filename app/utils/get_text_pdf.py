from typing import List

import pytesseract
from fastapi import HTTPException
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)

from .in_list import in_list
from .list_files import list_files


def extract_pdf_text(pdf_path: str) -> List[str]:
    """Extract text from a pdf by converting the pdf
       first to images and then to text.

    Args:
        pdf_path (str): pdf path on the machine

    Returns:
        List[str]: returns a list of the extracted text on each page.
    """
    file_name = pdf_path[len("/usr/src/app/files/pdf/"):]
    file_list = list_files()
    if not in_list(file_list, pdf_path):
        raise HTTPException(status_code=400, detail=f"PDF {file_name} not found")

    try:
        pages = convert_from_path(pdf_path, 500)
    except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while converting the pdf to images.\n\nError: {e}",
        )

    text_by_page: List = []
    for page in pages:
        try:
            text_by_page.append(pytesseract.image_to_string(page).replace("\n", " "))
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"An error occurred while extracting the text from the pdf.\n\nError: {e}",
            )
    return text_by_page
