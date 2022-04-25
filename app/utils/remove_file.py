import os
from typing import Any, Dict

from fastapi import HTTPException


def remove_file(file_name: str = None) -> Dict[str, Any]:
    """Delete a file by name.

    Args:
        file_name (str, optional): filename to delete. Defaults to None.

    Returns:
        Dict[str, Any]: _description_
    """
    files = os.listdir('/usr/src/app/files/pdf')

    if files and file_name is not None and file_name in files:
        for file in files:
            if file == file_name:
                path = f'/usr/src/app/files/pdf/{file}'
                try:
                    os.remove(path)
                    return {
                        'Deleted': True,
                        'Path': path
                    }
                except OSError as e:
                    raise HTTPException(
                        status_code=500,
                        detail=f'An error occurred while trying to remove the file.\n\nError: {e}'
                    )
    elif not files:
        raise HTTPException(status_code=404, detail='Files not found')

    return {'Deleted': False}
