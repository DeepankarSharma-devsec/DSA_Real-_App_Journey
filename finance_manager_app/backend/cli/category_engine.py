from typing import Dict, Any, List, Optional


# (name, type, monthly_budget)
DEFAULT_CATEGORIES = (
    ("Food", "expense", 8000),
    ("Rent", "expense", 15000),
    ("Shopping", "expense", 5000),
    ("Transport", "expense", 3000),
    ("Entertainment", "expense", 4000),
    ("Health", "expense", 2000),
    ("Salary", "income", None),
)


class CategoryEngine:
    """
    Manages all categories for the Finance Manager app.

    Uses:
    - Tuple for DEFAULT_CATEGORIES (fixed, ordered, immutable)
    - Set for uniqueness and fast membership checks
    - Dict for storing category metadata
    """

    def __init__(self) -> None:
        # name -> {type: "expense"/"income", monthly_budget: float|None}
        self._categories_dict: Dict[str, Dict[str, Any]] = {}

        # set of category names (for quick `in` checks, no duplicates)
        self._category_set = set()

        # load the default categories on startup
        self._load_defaults()

    def _load_defaults(self) -> None:
        """Load categories from DEFAULT_CATEGORIES tuple."""
        for name, ctype, budget in DEFAULT_CATEGORIES:
            self.add_category(name, ctype, budget)

    def add_category(
        self,
        name: str,
        ctype: str = "expense",
        monthly_budget: Optional[float] = None,
    ) -> None:
        """
        Add or update a category.

        - name: category label (e.g., 'Food')
        - ctype: 'expense' or 'income'
        - monthly_budget: optional float
        """
        normalized = name.strip()
        if not normalized:
            return

        self._categories_dict[normalized] = {
            "type": ctype,
            "monthly_budget": monthly_budget,
        }
        self._category_set.add(normalized)

    def remove_category(self, name: str) -> None:
        """Remove a category if it exists."""
        normalized = name.strip()
        if normalized in self._categories_dict:
            del self._categories_dict[normalized]
        self._category_set.discard(normalized)

    def exists(self, name: str) -> bool:
        """Check if a category exists."""
        return name.strip() in self._category_set

    def list_categories(self) -> List[str]:
        """Return all category names sorted alphabetically."""
        return sorted(self._category_set)

    def get_category_info(self, name: str) -> Optional[Dict[str, Any]]:
        """Return metadata for a category, or None if not found."""
        return self._categories_dict.get(name.strip())

    def list_by_type(self, ctype: str) -> List[str]:
        """Return all categories of a given type (e.g., 'expense', 'income')."""
        result: List[str] = []
        for name, meta in self._categories_dict.items():
            if meta.get("type") == ctype:
                result.append(name)
        return sorted(result)
