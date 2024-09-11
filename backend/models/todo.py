from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class ToDo(Base):
    __tablename__ = "to_do"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"), index=True)
    description: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="to_dos")
