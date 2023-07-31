import pypot.dynamixel
import time


class Motor:
    def __init__(self, motorRight = 4, motorLeft = 10, motorHead = 11):
        print(pypot.dynamixel.get_available_ports())
        self.ports = pypot.dynamixel.get_available_ports()
        if not (self.ports or self.ports[0] != "/dev/ttyAMAO"):
            self.available = False
            print('No port available for motor.')
        else:
            self.available = True
            try:
                #self.dxl_io = pypot.dynamixel.DxlIO(self.ports[0])
                self.dxl_io = pypot.dynamixel.DxlIO("/dev/ttyACM0")
            except:
              print('No motor detected (et c est la merde)!')
              self.dxl_io = pypot.dynamixel.DxlIO(self.ports[0])
            #print(self.dxl_io.scan())
            time.sleep(2)
            self.motorRight = motorRight
            self.motorRightAvailable = False
            self.motorLeft = motorLeft
            self.motorLeftAvailable = False
            self.motorHead = motorHead
            self.motorHeadAvailable = False
            self.initMotor(motorRight,motorLeft,motorHead)
            self.oldPositionhead = 0.0

    def initMotor(self, motorRight, motorLeft, motorHead):
        self.motorRight = motorRight
        self.motorRightAvailable = False
        self.motorLeft = motorLeft
        self.motorLeftAvailable = False
        self.motorHead = motorHead
        self.motorHeadAvailable = False
        if self.motorRight != 0:
            self.setMotorWheelMode(self.motorRight)
            self.motorRightAvailable = True
        if self.motorLeft != 0:
            self.setMotorWheelMode(self.motorLeft)
            self.motorLeftAvailable = True
        if self.motorHead != 0:
            self.setMotorJointMode(motorHead)
            self.motorHeadAvailable = True
            # self.dxl_io.set_wheel_mode((motorLeft,motorRight, motorHead))

    def printInfo(self):
        print(pypot.dynamixel.get_available_ports())
        print(self.dxl_io.scan())
        if self.available:
            if self.motorRightAvailable:
                print(self.dxl_io.get_control_mode((self.motorRight,)))
            if self.motorLeftAvailable:
                print(self.dxl_io.get_control_mode((self.motorLeft,)))
            if self.motorHeadAvailable:
                print(self.dxl_io.get_control_mode((self.motorHead,)))

    def moveHead(self, positionHead, headSpeed = 100.0):
        if self.available:
            if self.motorHead:
                targetpositionHead = float(positionHead)
                self.dxl_io.set_goal_position({self.motorHead: targetpositionHead})
                self.oldPositionhead = positionHead
                time.sleep(6)
            else:
                print("can't motor head not available")
        else:
            print("can't move no open port are available")

    def move(self, rightSpeed, leftSpeed, duration, continu):
        if self.available:
            if self.motorRightAvailable:
                print("move")
                self.dxl_io.set_moving_speed({self.motorRight: rightSpeed})
            else:
                print("can't motor right not available")
            if self.motorLeftAvailable:
                self.dxl_io.set_moving_speed({self.motorLeft: -leftSpeed})
            else:
                print("can't motor left not available")
            if not continu :
                time.sleep(duration)
                if self.motorRightAvailable:
                    self.dxl_io.set_moving_speed({self.motorRight: 0.0})
                if self.motorLeftAvailable:
                    self.dxl_io.set_moving_speed({self.motorLeft: 0.0})
        else:
            print("can't move no open port are available")

    def stop(self):
        if self.available:
            if self.motorRightAvailable:
                print("stop")
                self.dxl_io.set_moving_speed({self.motorRight: 0})
            if self.motorLeftAvailable:
                self.dxl_io.set_moving_speed({self.motorLeft: 0})
        else:
            print("can't move no open port are available")

    def setMotorWheelMode(self, motor):
        self.dxl_io.set_wheel_mode({motor})

    def setMotorJointMode(self, motor):
        self.dxl_io.set_joint_mode({motor})


if __name__ == '__main__':
    motor = Motor()
    #motor.printInfo()
    #motor.move(200,200,5,False)
    motor.moveHead(60)
