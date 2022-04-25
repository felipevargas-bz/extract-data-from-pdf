from typing import Any, Dict, List


def in_list(list: List, value_check: Any) -> bool:
    """Check if a value is in a list.

    Args:
        list (List): list to be checked.
        value_check (any): value to be checked.

    Returns:
        bool: True if the value is in the list, False otherwise.
    """
    if list and value_check and isinstance(list[0], Dict):
        for item in list:
            for value in item.values():
                if value_check == value:
                    return True
    elif list and value_check:
        return value_check in list

    return False
