from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Transaction:
    id: Optional[int] = None
    user_id: Optional[int] = None
    type: Optional[str] = None
    amount: Optional[float] = None
    category_id: Optional[int] = None
    created_at: Optional[datetime] = datetime.now()
    description: Optional[str] = None