from bierepong.extensions import Base, engine
from .sensor import Sensor

Base.metadata.create_all(engine)
