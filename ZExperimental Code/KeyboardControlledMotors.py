#from mobility import *
#import time
# import keyboard  # using module keyboard
#if __name__ == "__main__":

# Initialise motors
#MotorA = Motor(17,18)
#MotorB = Motor(22,23)
    
#Testing Pieces:
#while True:  # making a loop
#    try:  # used try so that if user pressed other than the given key error will not be shown
#        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
#            break  # finishing the loop
#    except:
#        break  # if user pressed a key other than the given key the loop will break

#     # Each motor can be controlled individually like so:
#     MotorA.forward(100)
#     time.sleep(1)
#     MotorA.stop()
#     time.sleep(1)
#     MotorA.backward(100)
#     time.sleep(1)
#     MotorA.stop()

#     # Or you can control both motors at the same time using the static methods:
#     Motor.moveForward(100)
#     time.sleep(1)
#     Motor.moveReverse(100)
#     time.sleep(1)
#     Motor.stopAll()
#     Motor.rotate(100)
#     time.sleep(1)
#     Motor.rotate(-100)
#     time.sleep(1)
#     Motor.stopAll()
    

    # The library also does the cleanup at the end of execution. So even while running, if the program ends
    # Motors *Should* stop automatically.
    # However, if you want to nicely clean up after yourself, the Motor.cleanup() method will make sure everything is nice and tidy when you're done

#     Motor.cleanup()


# ------------------------------ Experimental Code:
#pip3 install keyboard
import keyboard
while True:
    keyboard.wait("1")
    
    
    
# -------- Next code to run:
# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break



# ----------------- Next Code to run:
# import keyboard

# while True:
#     if keyboard.read_key() == "p":
#         print("You pressed p")
#         break
#     keyboard.write("\n The key '1' was pressed!")

# # =------------------------------------
# import keyboard
# keyboard.wait("p")
# print("You pressed p")

# # --------------------------------
# import keyboard

# while True:
#     if keyboard.is_pressed("p"):
#         print("You pressed p")

# -----------------------------------
# import curses

# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)

# try:
#     while True:
#         char = screen.getch()
#         if char == ord('q'):
#             break
#         elif char == curses.KEY_UP:
#             print('up')
#         elif char == curses.KEY_DOWN:
#             print('down')
#         elif char == curses.KEY_RIGHT:
#             print('right')
#         elif char == curses.KEY_LEFT:
#             print('left')
#         elif char == ord('s'):
#             print('stop')

# finally:
#     curses.nocbreak(); screen.keypad(0); curses.echo()
#     curses.endwin()
# #         break

# ----------------------------------
# # Camera Test Code
# from picamera import PiCamera
# import curses 
# from gpizero import Robot
# camera = PiCamera()
# camera.resolution = (640,480)
# camera.rotation = 180
# camera.start_preview()
# ---------------------------------------

# import pygame

# while True:
#     keys = pygame.key.get_pressed()
#     if (keys[pygame.K_LEFT]):
#         pos_x -= 5
#     elif (keys[pygame.K_RIGHT]):
#         pos_x += 5
#     elif (keys[pygame.K_UP]):
#         pos_y -= 5
#     elif (keys[pygame.K_DOWN]):
#         pos_y += 5
# ------------------------------------------------

