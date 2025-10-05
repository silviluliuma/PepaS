from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Transaction:
    id: Optional[int]
    user_id: Optional[int]
    type: str = ""
    amount: float = 0.0
    category_id: Optional[int]
    description: str = ""
    created_at: Optional[datetime]