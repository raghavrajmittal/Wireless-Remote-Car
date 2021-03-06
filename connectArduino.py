import serial
import time

arduino = None

def sendCommand(arduino, command):
    # print(direction)
    if command == 0:
        arduino.write(("F\n").encode())

    elif command == 1:
        arduino.write(("D\n").encode())

    elif command == 3:
        arduino.write(("R\n").encode())

    elif command == 2:
        arduino.write(("L\n").encode())

    elif command == 27:     # stop
        arduino.write(("S\n").encode())

def connect(port = '/dev/cu.usbserial-DN01DQRE'):
    global arduino
    arduino = serial.Serial(port, 9600, timeout=0.5)
    time.sleep(1)
    return arduino

def disconnect(arduino):
    arduino.close()
