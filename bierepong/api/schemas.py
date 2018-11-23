from marshmallow import Schema, fields


class SensorSchema(Schema):
    id = fields.Integer(dump_only=True)
    status = fields.String()


sensor_schema = SensorSchema()
sensors_schema = SensorSchema(many=True)
