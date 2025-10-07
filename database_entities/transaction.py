from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Transaction:
    id: Optional[int]
    user_id: Optional[int]
    type: str
    amount: float
    category_id: Optional[int]
    created_at: Optional[datetime]
    description: str = ""