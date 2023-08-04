import board
import busio
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X
import threading

i2c = board.I2C()

class Lidar:
    def __init__(self, PIN_XSHUT, I2C_ADDRESS, TIMING_BUDGET=200000):
        self.I2C_ADDRESS = I2C_ADDRESS
        self.PIN_XSHUT = PIN_XSHUT
        self.TIMING_BUDGET = TIMING_BUDGET
        self.distance = 0 # distance in cm
        
        # i2c bus initialization
        i2c = board.I2C()
        
        # sensor initialization
        self.PIN_XSHUT.switch_to_output(value=False)
        self.PIN_XSHUT.value = True
        
        self.SENSOR = VL53L0X(i2c)
        self.SENSOR.set_address(self.I2C_ADDRESS)
        self.SENSOR.measurement_timing_budget = 400000
        
        self,SENSOR.start_continous()

    def __repr__(self):
        return f"Lidar-PIN:{self.PIN_XSHUT},ADDRESS:{self.I2C_ADDRESS}"
    
    def activate_sensor(self):
        self.PIN_XSHUT.value = True

    
    def deactivate_sensor(self):
        self.PIN_XSHUT.value = False
    
    def get_distance(self):
        try:
            self.distance = self.SENSOR.range / 10 
        except:
            self.distance = 0
        
        return self.distance
        
        
