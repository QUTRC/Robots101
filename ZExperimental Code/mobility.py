import RPi.GPIO as GPIO

# Initialise the GPIO pins in desired mode. Probably a redundant step, but best to be safe.

GPIO.setmode(GPIO.BCM)


#####################################################################################################################################################
# This is the mobility sub-system library. This library is designed to be imported into a main.py file and used like any other library.
# Instructions for use:
# 1. Import the library into your main.py file using from mobility import *
# 2. Create an instance of the Motor class for each motor using MotorA = Motor(forwardPin,reversePin) etc.
# 3. Use the motor instance to move the motor in the desired direction using motor.forward() or motor.reverse() (Note that throttle values can be used, but are optional and are set to
#                                                                                      100% if not used) 
# 4. Use the motor instance to stop the motor using motor.stop()
# 5. In order to control both motors at the same time, use Motor.moveForward(speed) or Motor.moveReverse(speed)
# 6. In order to stop all motors at the same time, use Motor.stopAll()
# 7. In order to clean up after yourself, use Motor.cleanup()
# 8. If you want to use the library in a main.py file, you can use the following code:
#####################################################################################################################################################


# Define a Motor class. This will be used to control the motors individually, but through the use of static methods, can also be used to control
# the whole mobility sub-system holistically. I can show you how they work in the main.py file. Let me know if you want me to show you classes work
# in more detail Luc. >:)

class Motor():

    Motors = []

    def __init__(self, pinForward: int, pinReverse: int):
        if len(Motor.Motors) >=2:
            raise Exception("Only two motors allowed!")
        Motor.Motors.append(self)
        self.pinForward = pinForward
        self.pinReverse = pinReverse
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinReverse, GPIO.OUT)
        
        GPIO.output(self.pinForward, GPIO.LOW)
        GPIO.output(self.pinReverse, GPIO.LOW)

        self.forwardPWM = GPIO.PWM(self.pinForward, 100)
        self.reversePWM = GPIO.PWM(self.pinReverse, 100)

        self.forwardPWM.start(0)
        self.reversePWM.start(0)

    def forward(self, throttle=100):
        self.forwardPWM.ChangeDutyCycle(throttle)
        self.reversePWM.ChangeDutyCycle(0)
        
    
    def backward(self, throttle=100):
        self.forwardPWM.ChangeDutyCycle(0)
        self.reversePWM.ChangeDutyCycle(throttle)
    
    def stop(self):
        self.forwardPWM.ChangeDutyCycle(0)
        self.reversePWM.ChangeDutyCycle(0)
    
    @staticmethod
    def cleanup():
        Motor.stopAll()
    
    @staticmethod
    def moveForward(throttle=100):
        for motor in Motor.Motors:
            motor.forward(throttle)

    @staticmethod
    def moveReverse(throttle=100):
        for motor in Motor.Motors:
            motor.backward(throttle)

    @staticmethod
    def rotate(dir: int):
        if dir > 0:
            Motor.Motors[0].forward(dir)
            Motor.Motors[1].backward(dir)
        else:
            Motor.Motors[0].backward(abs(dir))
            Motor.Motors[1].forward(abs(dir))

    @staticmethod
    def stopAll():
        for motor in Motor.Motors:
            motor.stop()
    
    def __del__(self):
        Motor.cleanup()
    