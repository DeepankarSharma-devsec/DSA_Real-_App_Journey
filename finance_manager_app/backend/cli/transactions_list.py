from datetime import datetime
from typing import List
from transaction import Transaction


class TransactionList:
    """
    Manages a collection of Transaction objects.

    This is the in-memory list engine for the Finance Manager app.
    """

    def __init__(self) -> None:
        # internal storage, just a simple Python list
        self._transactions: List[Transaction] = []

    # ---------- Core CRUD-style methods ----------

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a new transaction to the list."""
        self._transactions.append(transaction)

    def all(self) -> List[Transaction]:
        """
        Return a copy of all transactions.

        Returning a copy avoids accidental external modification.
        """
        return list(self._transactions)

    # ---------- Aggregations ----------

    def total_amount(self) -> float:
        """Return the sum of all transaction amounts."""
        total = 0.0
        for t in self._transactions:          # loop from today’s topic
            total += t.amount
        return total

    # ---------- Filters ----------

    def filter_by_category(self, category: str) -> List[Transaction]:
        """Return all transactions in a given category."""
        return [t for t in self._transactions if t.category == category]

    def filter_by_min_amount(self, min_amount: float) -> List[Transaction]:
        """Return transactions with amount >= min_amount."""
        return [t for t in self._transactions if t.amount >= min_amount]

    def filter_by_date_range(self, start_date: str, end_date: str) -> List[Transaction]:
        """
        Filter transactions between two dates (inclusive).

        Dates are expected in YYYY-MM-DD format.
        """
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()

        result: List[Transaction] = []
        for t in self._transactions:
            t_date = datetime.strptime(t.date, "%Y-%m-%d").date()
            if start <= t_date <= end:        # conditional from today’s topic
                result.append(t)

        return result
