import serial


def send(msg):
    ser = serial.Serial('/dev/tty.usbserial', 9600)
    ser.write(data=msg)
    ser.close()
