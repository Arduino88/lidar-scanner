from machine import Pin, PWM


class Servo():
    def __init__(self, pin: int):
        self.servo_pwm = PWM(Pin(pin), freq=50, duty=130)
        self.range = (28, 130)
        self.angle_range = (0, 180)

    def convert(self, val: int) -> int:
        val /= self.angle_range[1]
        val *= (self.range[1] - self.range[0])
        val += self.range[0]
        return round(val)

    def write(self, angle):
        if self.angle_range[0] <= angle <= self.angle_range[1]:
            self.servo_pwm.duty(self.convert(angle))
