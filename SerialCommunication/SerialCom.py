import threading
import time
import serial
import sys
import glob
from soundControl.sound import *


class SerialCom(threading.Thread):
    def __init__(self, threadID, name, port = '/dev/ttyACM1', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.running = True
        self.open = False
        self.available = False
        availablePort = self.serial_ports()
        print(availablePort)
        for p in availablePort:
            if p.startswith('/dev/ttyACM'):
                print("start with good start")
                self.available = True
        if self.available:
            try:
                self.ser = serial.Serial(
                    port=port,
                    baudrate=baudrate,
                    parity=parity,
                    stopbits=stopbits,
                    bytesize=bytesize
                )
                """parity=parity,
                    stopbits=stopbits,
                    bytesize=bytesize"""
                #self.ser.write("testOpen")
            except IOError as e:
                print(e)

        else:
            print("no port available")
            self.ser = None


    def run(self):
        while self.running:
            self.open = self.initSerial()

            try:
                while True:
                    if self.open:
                        input = self.ser.readline()
                        if(input != ""):
                            print(input)
                            if(input == "test"):
                                print("receive test")
                            elif(input == "knock"):
                                print("knock received from arduino")
                                playSound("sensor/sensor1.ogg")
                            elif (input == "knock\\r\\n'"):
                                print("knock r n double anti slash received from arduino")
                                playSound("sensor/sensor1.ogg")
                            elif (input == "knock\r\n"):
                                print("knock r n received from arduino")
                                playSound("sensor/sensor1.ogg")
                            elif (input == b"knock"):
                                print("knock received bite from arduino")
                                playSound("sensor/sensor1.ogg")
                            elif (input == b"knock\\r\\n'"):
                                print("knock r n bite double anti slash received from arduino")
                                playSound("sensor/sensor1.ogg")
                            elif (input == b"knock\r\n"):
                                print("knock r n bite received from arduino")
                                playSound("sensor/sensor1.ogg")
                        time.sleep(1)
            except IOError:
                pass
            self.closeSerial()

    def write(self, data):
        if self.open:
            #maybe need ths line:
            #self.ser.write(data + '\r\n')
            print("send this : " + str(data))
            self.ser.write(data)
            #self.ser.write(str(data))

    def initSerial(self):
        if self.available:
            self.ser.isOpen()
            self.open = True
        return self.open

    def closeSerial(self):
        if self.available:
            self.ser.close()
            self.open = False

    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

if __name__ == '__main__':
    serialCom = SerialCom(1, "serialThread")

    serialCom.daemon = True
    serialCom.start()

    while True:
        time.sleep(1)
        print(serialCom.serial_ports())
        serialCom.write("lightOn")
        time.sleep(3)
        serialCom.write("lightOff")
        time.sleep(3)
        #serialCom.write("testtestest" + "\r\n")