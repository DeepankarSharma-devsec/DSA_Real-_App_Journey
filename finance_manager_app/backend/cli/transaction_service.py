from datetime import datetime
from typing import Optional

from transaction import Transaction
from transactions_list import TransactionList
from category_engine import CategoryEngine


# -------- Custom Exceptions --------

class TransactionError(Exception):
    """Base class for all transaction-related errors."""
    pass


class InvalidAmountError(TransactionError):
    """Raised when amount is missing, non-numeric, or <= 0."""
    pass


class InvalidCategoryError(TransactionError):
    """Raised when category is empty or not registered in CategoryEngine."""
    pass


class InvalidDateError(TransactionError):
    """Raised when date is missing or not in YYYY-MM-DD format."""
    pass


# -------- Service Layer --------

class TransactionService:
    """
    Service layer responsible for creating and validating transactions.

    - Applies validation rules.
    - Uses custom exceptions.
    - Adds valid Transaction objects into a TransactionList.
    """

    def __init__(self, t_list: TransactionList, category_engine: CategoryEngine) -> None:
        self._t_list = t_list
        self._category_engine = category_engine

    # ----- Internal validators (encapsulation) -----

    def _validate_amount(self, amount: float) -> float:
        """Ensure amount is a positive numeric value."""
        try:
            value = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Amount must be a valid number.")

        if value <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        return value

    def _validate_category(self, category: str) -> str:
        """Ensure category is non-empty and exists in CategoryEngine."""
        if category is None:
            raise InvalidCategoryError("Category is required.")

        normalized = category.strip()
        if not normalized:
            raise InvalidCategoryError("Category cannot be empty.")

        if not self._category_engine.exists(normalized):
            raise InvalidCategoryError(f"Unknown category: {normalized}")

        return normalized

    def _validate_date(self, date_str: Optional[str]) -> str:
        """
        Ensure date is either:
        - None → use today's date
        - Or a valid 'YYYY-MM-DD' string
        """
        if date_str is None:
            return datetime.now().strftime("%Y-%m-%d")

        try:
            parsed = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise InvalidDateError("Date must be in 'YYYY-MM-DD' format.")

        # Normalize format
        return parsed.strftime("%Y-%m-%d")

    # ----- Public API -----

    def create_transaction(
        self,
        amount: float,
        category: str,
        date: Optional[str] = None,
        note: str = "",
    ) -> Transaction:
        """
        Validate inputs, create a Transaction, and add it to the list.

        Raises:
        - InvalidAmountError
        - InvalidCategoryError
        - InvalidDateError
        """
        valid_amount = self._validate_amount(amount)
        valid_category = self._validate_category(category)
        valid_date = self._validate_date(date)
        valid_note = note or ""

        tx = Transaction(
            amount=valid_amount,
            category=valid_category,
            date=valid_date,
            note=valid_note,
        )
        self._t_list.add_transaction(tx)
        return tx

    def safe_create_transaction(
        self,
        amount: float,
        category: str,
        date: Optional[str] = None,
        note: str = "",
    ) -> Optional[Transaction]:
        """
        Safe wrapper around create_transaction.

        - Catches TransactionError
        - Prints a friendly message
        - Returns None if creation failed

        This demonstrates try/except usage in a real context.
        """
        try:
            return self.create_transaction(amount, category, date, note)
        except TransactionError as ex:
            # In future this could log to a file instead of print
            print(f"[TransactionService] Failed to create transaction: {ex}")
            return None
