from datetime import datetime
from typing import Dict,Any,Optional

class Transaction:

    def __init__(
            self,
            amount: float,
            category: str,
            date: Optional[datetime]=None,
            note: Optional[str]=None,
    ) -> None:
        
        self.amount=float(amount)
        self.category=category

        if date is None:
            self.date=datetime.now().strftime("%Y-%m-%d")
        else:
            self.date=date
        
        self.note=note

    
    def to_dict(self) -> Dict[str,Any]:
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note,
        }
    
    def __repr__(self) -> str:

        return(
            f"<Transaction amount={self.amount}"
            f" category={self.category}' "
            f"date={self.date}'>"
        )

    def __str__(self) -> str:

        return f"{self.date} | {self.category:<12} | ₹{self.amount:.2f} | {self.note}" 
        


