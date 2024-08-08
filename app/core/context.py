from dataclasses import dataclass
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Database


@dataclass
class ApplicationContext:
    database: Optional[Database] = None
    session: Optional[AsyncSession] = None
