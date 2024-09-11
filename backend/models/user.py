from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .todo import ToDo

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
    password_salt: Mapped[str]

    to_dos: Mapped[list["ToDo"]] = relationship(back_populates="user")
    