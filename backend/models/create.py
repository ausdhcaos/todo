from .db_session import engine
from .base import Base
        
def create_db():
    Base.metadata.create_all(engine)