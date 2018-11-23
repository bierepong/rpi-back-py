import time

from bierepong.controllers import SensorControler
from bierepong.models import Sensor

SENSOR_THRESHOLD = 10


def handle_sensor(ctrl, sensor_id, sensor_value):
    print(f'{sensor_id} => {sensor_value}')
    if not sensor_id.isdigit() or not sensor_value.isdigit():
        return
    sensor_id = int(sensor_id)
    sensor_value = int(sensor_value)
    sensor_status = 'OK' if sensor_value > SENSOR_THRESHOLD else 'KO'
    sensor = ctrl.get(obj_id=sensor_id)
    if sensor is None:
        sensor = Sensor(id=sensor_id, status=sensor_status)
        ctrl.save(obj=sensor)
    elif sensor.status != sensor_status:
        sensor.status = sensor_status
        ctrl.save(obj=sensor)


def listen():
    # ser = serial.Serial('/dev/tty.usbserial', 9600)
    sensor_controller = SensorControler()
    while True:
        # line = ser.readline()
        line = '0:5;1:100;2:200;3:5'
        for sensor_id, sensor_value in [token.split(':') for token in line.split(';')]:
            handle_sensor(ctrl=sensor_controller, sensor_id=sensor_id, sensor_value=sensor_value)
        time.sleep(10)


if __name__ == '__main__':
    listen()
