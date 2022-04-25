import re
from typing import Dict

from fastapi import HTTPException


def extract_data_pdf(text: str, path: str) -> Dict[str, str]:
    """Extract data from a pdf whose text is passed as an argument.

    Args:
        text (str): PDF text.
        path (str): path of the pdf on the machine.

    Returns:
        Dict[str, str]: returns a dictionary with the information
                        extracted from the text.
    """

    try:
        VendorName = re.search(r"(?<=(V|v)endor (N|n)ame: )(.+)(?=F)", text)
        FiscalNumber = re.search(
            r"(?<=(F|f)iscal (N|n)umber: )(.+)? (?=Contract)", text
        )
        Contract = re.search(r"((?<=Contract #:)|(?<=Contract#:))(\s\d+)(?= S)", text)
        StartDate = re.search(r"(?<=Start date:)(.+)(?= E)", text)
        EndDate = re.search(r"(?<=End date:)(.+?)(?= .)", text)
        Comment = re.search(r"(?<=Comments:)(.+?)(?=M)", text)
    except TypeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while extracting the information from the pdf.\n\nError: {e}",
        )

    return {
        "Vendor_Name": VendorName.group() if VendorName and VendorName.group() else "",
        "Fiscal_Number": FiscalNumber.group()
        if FiscalNumber and FiscalNumber.group()
        else "",
        "Contract": Contract.group() if Contract and Contract.group() else "",
        "Start_Date": StartDate.group() if StartDate and StartDate.group() else "",
        "End_date": EndDate.group() if EndDate and EndDate.group() else "",
        "Comments": Comment.group() if Comment and Comment.group() else "",
        "Doc_Path": path,
    }
