from bierepong.extensions import Session
from bierepong.models import Sensor


class DefaultController:
    model_cls = None

    def get_session(self):
        return Session()

    def get(self, obj_id):
        return self.get_session().query(self.model_cls).get(obj_id)

    def list(self, limit=None, **filters):
        query = self.get_session().query(self.model_cls).filter_by(**filters)
        if limit:
            query = query.limit(limit)
        return query.all()

    def delete(self, limit=None, **filters):
        session = self.get_session()
        if limit:
            query = session.query(self.model_cls.id).filter_by(**filters).limit(limit).subquery()
            session.query(self.model_cls).filter(self.model_cls.id.in_(query)).delete(synchronize_session='fetch')
            session.commit()
            return

        query = session.query(self.model_cls).filter_by(**filters)
        query.delete()
        session.commit()

    def delete_obj(self, obj):
        session = self.get_session()
        session.delete(obj)
        session.commit()

    def save(self, obj):
        session = self.get_session()
        session.add(obj)
        session.commit()

    def bulk_save(self, obj_list):
        session = self.get_session()
        session.bulk_save_objects(obj_list)
        session.commit()


class SensorControler(DefaultController):
    model_cls = Sensor
