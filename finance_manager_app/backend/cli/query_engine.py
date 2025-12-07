from typing import List
from transactions_list import TransactionList
from transaction import Transaction


class QueryEngine:
    """
    Functional-style querying layer on top of TransactionList.

    Uses lambda, map, and filter to:
    - filter by category
    - filter by month (YYYY-MM)
    - filter by amount range
    - extract months from all transactions
    """

    def __init__(self, transaction_list: TransactionList) -> None:
        self._t_list = transaction_list

    def _all(self) -> List[Transaction]:
        """Internal helper to get all transactions from the list."""
        return self._t_list.all()

    # ---------- Filters ----------

    def filter_by_category(self, category: str) -> List[Transaction]:
        """
        Return all transactions that match the given category.
        Uses filter + lambda.
        """
        return list(filter(lambda t: t.category == category, self._all()))

    def filter_by_month(self, month_str: str) -> List[Transaction]:
        """
        Return all transactions for a specific month.

        month_str should be in 'YYYY-MM' format, e.g. '2025-12'.
        Uses filter + lambda with date prefix matching.
        """
        return list(filter(lambda t: t.date.startswith(month_str), self._all()))

    def filter_by_amount_range(self, min_amount: float, max_amount: float) -> List[Transaction]:
        """
        Return all transactions where min_amount <= amount <= max_amount.
        Uses filter + lambda with a compound condition.
        """
        return list(
            filter(
                lambda t: (t.amount >= min_amount) and (t.amount <= max_amount),
                self._all(),
            )
        )

    # ---------- Transformations ----------

    def extract_months(self) -> List[str]:
        """
        Return a list of 'YYYY-MM' strings for all transactions.

        Uses map + lambda to transform Transaction -> month string.
        """
        return list(map(lambda t: t.date[:7], self._all()))

    def extract_amounts(self) -> List[float]:
        """
        Return all transaction amounts as a list of floats.
        Uses map + lambda.
        """
        return list(map(lambda t: t.amount, self._all()))
