import os
from typing import Dict, List

from fastapi import HTTPException


def list_files(file_name: str = None) -> List[Dict[str, str]]:
    """list all the pdf files in the path /usr/src/app/files/pdf
       or if a filename was passed it returns the path of that file and its name.

    Args:
        file_name (str, optional): name of the file to which you want to get the path. Defaults to None.

    Returns:
        List[Dict[str, str]]: list of found pdf files.
    """

    if file_name and ".pdf" not in file_name:
        raise HTTPException(status_code=400, detail="File must be a PDF")
    path = "/usr/src/app/files/pdf/"
    try:
        file_list = os.listdir(path)
    except OSError as e:
        raise HTTPException(
            status_code=400,
            detail=f"An error occurred while trying to list the files.\n\nError: {e}",
        )

    if file_list and file_name is not None and file_name in file_list:
        for file in file_list:
            if file == file_name:
                return [{"Path": f"/usr/src/app/files/pdf{file}", "file_name": file}]
    elif file_list and file_name and file_name not in file_list:
        raise HTTPException(status_code=400, detail=f"File {file_name} not found")
    else:
        files = (
            [
                {"Path": f"/usr/src/app/files/pdf/{str(file)}", "file_name": str(file)}
                for file in file_list
            ]
            if file_list
            else None
        )

        if files:
            return files
        else:
            raise HTTPException(status_code=404, detail="Files not found")
    return [{}]
