import socket
import time

class SocketControl():
    '''Simple Class to send commands to relay for waterpump'''
    # Relay Commands
    TURN_ON_RELAY = '\xfe\x00'
    TURN_OFF_RELAY = '\xfe\x08'

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.connected = False
        
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            self.connected = True
        except Exception:
            print('Failed to connect to {}'.format(self.ip))

    def send_cmd(self, cmd):
        '''Sends command through the socket'''
        response = None
        if self.connected:
            self.sock.send(cmd + '\r')
            response = self.sock.recv(4096)
        return response      

    def power_on(self):
        '''Turns on the relay'''
        return self.send_cmd(self.TURN_ON_RELAY)

    def power_off(self):
        '''Turns off the relay'''
        return self.send_cmd(self.TURN_OFF_RELAY)      
        
if __name__ == '__main__':
    # Device Settings
    ip = '192.168.1.20'
    port = 2101

    test_dev = SocketControl(ip, port)
    test_dev.power_on()
    time.sleep(3)
    test_dev.power_off()
    del test_dev