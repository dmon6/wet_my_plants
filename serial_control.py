import serial
import time

class SerialControl():
    '''Simple serial control'''
    TURN_ON = chr(254) + chr(1) + chr(0)
    TURN_OFF = chr(254) + chr(0)
    WAIT = .3

    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.baud = 9600
        
    def send_cmd(self, cmd):
        '''Combined the connection and send because I'm lazy'''
        returned_data = None
        with serial.Serial(self.serial_port, self.baud)as s:
            s.write(cmd)
            time.sleep(WAIT)
            returned_data = s.recv(256)
        return returned_data

    def turn_on(self):
        '''Turns on the relay'''
        return self.send_cmd(TURN_ON)

    def turn_on(self):
        '''Turns off the relay'''
        return self.send_cmd(TURN_OFF)

if __name__ == '__main__':
    serial_port = '/dev/ttyS0'
    s = SerialControl(serial_port)
    s.turn_on()
    time.sleep(4)
    s.turn_off()

