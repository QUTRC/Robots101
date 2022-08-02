# This is a PID class that can be used to control a system.
# Step 1. Initialise with variableName = PID(P, I, D, maxOutput, minOutput)
# Step 2. Call the update method with the current value of the system.
# Step 3. The update method returns the output of the PID controller.
# e.g throttle = variableName.update(targetValue, currentValue, dt)

class PID():
    # This just sets the constants we need to run the controller. Nothing fancy
    def __init__(self, kp: float, ki: float, kd: float, max: float, min: float):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max = max
        self.min = min
        self.last_error = 0
        self.integral = 0
        self.ISaturation = [self.max, self.min]

    # This rests the controller. Use this when you want to stop the system and reset the controller.
    def reset(self):
        self.last_error = 0
        self.integral = 0

    def update(self, target: float, current: float, dt: float) -> float:
        self.error = target - current

        # Calculate the integral by adding the error to the previous integral
        self.integral += self.error * dt

        # One issue with the I term, is that it can get really big really fast. We stop this by setting a saturation point to clamp the system to avoid overshoot.
        self.integral = self.ISaturation[0] if self.integral > self.ISaturation[1] else self.integral

        # Calculate the derivative by subtracting the error from the previous error and dividing by the change in time
        derivative = (self.error - self.last_error) / dt

        # Proportional gain is just Error * Kp. This is the most important part of the PID controller as it is the term that moves the system towards the
        # target.
        self.P = self.kp * self.error

        # Integral gain is the sum of all the errors multiplied by Ki. This is the part of the controller that tries to keep the system from drifting and fights external forces
        # like gravity and friction.
        self.I = self.ki * self.integral

        # The derivative gain is the rate of change of the error multiplied by Kd. This is the part of the controller that tries to keep the system from overshooting the target.
        self.D = self.kd * derivative

        # The output is the sum of the three terms above.
        output = self.P + self.I + self.D
        self.last_error = self.error

        # We just clamp the output value to the max and minimum values specified when the PID controller was created.
        output = max(min(output, self.max), self.min)
        return output