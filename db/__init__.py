from .tables import Base
from .base import engine

Base.metadata.create_all(engine)
