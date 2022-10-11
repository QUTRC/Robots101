from mobility import *
import time
import keyboard  # using module keyboard
if __name__ == "__main__":

# Initialise motors
MotorA = Motor(17,18)
MotorB = Motor(22,23)
    
#Testing Pieces:
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break

    # Each motor can be controlled individually like so:
    MotorA.forward(100)
    time.sleep(1)
    MotorA.stop()
    time.sleep(1)
    MotorA.backward(100)
    time.sleep(1)
    MotorA.stop()

    # Or you can control both motors at the same time using the static methods:
    Motor.moveForward(100)
    time.sleep(1)
    Motor.moveReverse(100)
    time.sleep(1)
    Motor.stopAll()
    Motor.rotate(100)
    time.sleep(1)
    Motor.rotate(-100)
    time.sleep(1)
    Motor.stopAll()
    

    # The library also does the cleanup at the end of execution. So even while running, if the program ends
    # Motors *Should* stop automatically.
    # However, if you want to nicely clean up after yourself, the Motor.cleanup() method will make sure everything is nice and tidy when you're done

    Motor.cleanup()