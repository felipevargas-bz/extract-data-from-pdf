from fastapi import HTTPException


def save_file(filename: str, data) -> str:
    """Save a file to the server

    Args:
        filename (str): name of the file to save
        data (_type_): file data to save

    Returns:
        str: returns the path of the saved file.
    """

    try:
        with open(f"/usr/src/app/files/pdf/{filename}", "wb") as f:
            f.write(data)

        return f"/usr/src/app/files/pdf/{filename}"
    except OSError as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while trying to save the pdf Error: {e}",
        )
