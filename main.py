""" demo example """

from motor.py import *
from time import *
from threading import *

if __name__ == '__main__':
    motor = Motor()
    while True:
    	th = Thread(target=motor.move(200,200,2,False))
    	th.daemon = True
    	th.start()
    	motor.move(200,200,2,False)
    	motor.move(-200,-200,2,False)
    	time.sleep(120)