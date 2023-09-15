import board
from adafruit_vl53l0x import VL53L0X
from statistics import mean
import time

# i2c bus initialization
i2c = board.I2C()
    
class Lidar:
    def __init__(self, PIN_XSHUT, I2C_ADDRESS, TIMING_BUDGET=200000):
        self.I2C_ADDRESS = I2C_ADDRESS
        self.PIN_XSHUT = PIN_XSHUT
        self.TIMING_BUDGET = TIMING_BUDGET
        self.distance = 0 # distance in cm
        self.CONSTANT = None
        self.STATUS = 0
        
        # sensor initialization
        count_initialization = 0
        while self.STATUS == 0 or count_initialization > 3:
            try:
                self.PIN_XSHUT.switch_to_output(value=False)
                self.PIN_XSHUT.value = True
                time.sleep(1)
                
                self.SENSOR = VL53L0X(i2c)
                time.sleep(0.5)
                
                self.SENSOR.set_address(self.I2C_ADDRESS)
                time.sleep(0.3)
                
                self.SENSOR.measurement_timing_budget = 400000
                time.sleep(0.3)
                
                self.SENSOR.start_continuous()
                self.CONSTANT = self.calculate_constant()
                self.STATUS = 1
            except OSError:
                print("Initialization Error")
                self.STATUS = 0
                count_initialization += 1
                
        print(self.I2C_ADDRESS)
            
    def __repr__(self):
        return f"Lidar-PIN:{self.PIN_XSHUT},ADDRESS:{self.I2C_ADDRESS},STATUS:{self.STATUS}"

    def status(self):
        return self.STATUS
    
    def activate_sensor(self) -> None:
        self.PIN_XSHUT.value = True

    def deactivate_sensor(self) -> None:
        self.PIN_XSHUT.value = False

    def calculate_constant(self) -> float:
        measurements = list()
        for _ in range(18):
            time.sleep(0.07)
            measurements.append(self.SENSOR.range / 10)
        return mean(measurements)
    
    def get_distance(self) -> float:
        try:
            # get distance in milimeters
            self.distance = self.SENSOR.range / 10
            if type(self.distance) == None:
                return -1
            # print(self.distance)
            return abs(round(self.distance - self.CONSTANT, 1))
        except OSError:
            print(OSError)
            # print(self.CONSTANT)
        
    