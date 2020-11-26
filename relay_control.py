import socket

class SocketControl():
    '''Simple Class to send commands to relay for waterpump'''
    # Relay Commands
    TURN_ON_RELAY = '\xfe\x00'
    TURN_OFF_RELAY = '\xfe\x08'

    def __init__(self, device_ip, device_port):
        self.device_ip = device_ip
        self.device_port = device_port
        self.connected = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(1)
        
        try:
            self.sock.connect((self.device_ip, self.device_port))
            self.connected = True
        except Exception:
            print('Failed to connect to {}'.format(self.device_ip))

    def send_cmd(self, cmd):
        if self.connected:
            self.sock.send(cmd + '\r')
            response = self.sock.recv(4096)
        return response      

    def power_on(self):
        return self.send_cmd(self.TURN_ON_RELAY)

    def power_off(self):
        return self.send_cmd(self.TURN_OFF_RELAY)      
        
if __name__ == '__main__':
    # Device Settings
    device_ip = '192.168.1.20'
    device_port = 10001

    
