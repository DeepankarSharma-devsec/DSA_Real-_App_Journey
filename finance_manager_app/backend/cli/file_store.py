import json
import os
from typing import Union

from transaction import Transaction
from transactions_list import TransactionList


def save_transactions_to_json(t_list: TransactionList, filepath: Union[str, os.PathLike]) -> None:
    """
    Save all transactions from a TransactionList into a JSON file.

    - Uses json from Python's standard library.
    - Creates parent directories if they don't exist.
    """
    # Ensure parent directory exists
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Convert all transactions to dictionaries
    data = [t.to_dict() for t in t_list.all()]

    # Write to JSON file with UTF-8 encoding
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_transactions_from_json(filepath: Union[str, os.PathLike]) -> TransactionList:
    """
    Load transactions from a JSON file and return a TransactionList.

    - If file does not exist, returns an empty TransactionList.
    """
    t_list = TransactionList()

    if not os.path.exists(filepath):
        # No file yet → return empty list (first run scenario)
        return t_list

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Reconstruct Transaction objects
    for item in data:
        t = Transaction(
            amount=item.get("amount", 0),
            category=item.get("category", "Unknown"),
            date=item.get("date"),              # uses default in class if None
            note=item.get("note") or "",        # ensure string
        )
        t_list.add_transaction(t)

    return t_list
