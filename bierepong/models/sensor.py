from sqlalchemy import Column, Integer, String

from bierepong.extensions import Base


class Sensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, )
    status = Column(String)

    def __str__(self):
        return f'[{self.id}]{self.status}'

    def __repr__(self):
        return self

    def to_json(self):
        return {
            "id": self.id,
            "status": self.status
        }
