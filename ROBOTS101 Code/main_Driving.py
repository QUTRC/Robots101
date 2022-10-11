from mobility import *
import time
if __name__ == "__main__":



    # Initialise motors
    MotorA = Motor(17,18)
    MotorB = Motor(22,23)

if cv2.waitKey(1) & 0xFF == ord('up'):      # Press lowercase Q on keyboard to exit
    print ("up")
        break
  
  else: 
    print("No Feed")
    
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


#----------------------------- My code from Tinkercad:


if 

void loop()
{
   if (IrReceiver.decode(&results))
    {
     Serial.println(results.value, HEX);
     if(results.value == 0xFD807F) // Vol +
      {
       pos=1600;
       LeftServo.write(pos);
       RightServo.write(pos);
      }
     else if(results.value == 0xFD906F) //Vol -
      {
       pos=1400;
       LeftServo.write(pos);
       RightServo.write(pos);
      }
     else if(results.value == 0xFD20DF) //Chapter skip left
      {
       LeftServo.write(1400);
       RightServo.write(1600);
      }
     else if(results.value == 0xFD609F) //Chapter skip right
      {
       LeftServo.write(1600);
       RightServo.write(1400);
      }
     else if(results.value == 0xFDA05F) //Stop (play/pause)
      {
       pos=1500;
       LeftServo.write(pos);
       RightServo.write(pos);
      }
     else if(results.value == 0xFDA857) //Turbo (5)
      {
       pos=2000;
       LeftServo.write(pos);
       RightServo.write(pos);
      }
     }
  irrecv.resume(); // Receive the next value
  delay(100);
}