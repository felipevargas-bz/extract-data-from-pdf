from fastapi import File, HTTPException, UploadFile

from app.schemas import ContentFile


def check_filePDF(file: UploadFile = File(...)) -> ContentFile:
    """Verify that the sent file is a pdf

    Returns:
        ContentFile: returns an object of the ContactFile class with the
                     name and content of the pdf file.
    """
    contents = file.file.read()
    if '.pdf' not in file.filename:
        raise HTTPException(status_code=400, detail='File must be a PDF')

    return ContentFile(**{'name': str(file.filename), 'contents': contents})
