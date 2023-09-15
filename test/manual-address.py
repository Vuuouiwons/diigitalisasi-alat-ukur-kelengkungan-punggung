import time
import board
from digitalio import DigitalInOut
import adafruit_vl53l0x

i2c = board.I2C()

xshut = [
    DigitalInOut(board.D4),
    DigitalInOut(board.D17),
    DigitalInOut(board.D27),
    DigitalInOut(board.D22),
    DigitalInOut(board.D10),
    DigitalInOut(board.D9),
    DigitalInOut(board.D21),
    DigitalInOut(board.D5),
    DigitalInOut(board.D6),
    DigitalInOut(board.D13),
    DigitalInOut(board.D19),
    DigitalInOut(board.D26),
    DigitalInOut(board.D23),
    DigitalInOut(board.D24),
    DigitalInOut(board.D25) # add more VL53L0X sensors by defining their SHDN pins here
]
 
for index, power_pin in enumerate(xshut):
    power_pin.switch_to_output(value=False)
    power_pin.value = False
    
sensors = list()

time.sleep(3)

for index, power_pin in enumerate(xshut):
    print(index)
    # if index == 6:
    #     continue
    
    power_pin.value = True
    time.sleep(1)
    sensor = adafruit_vl53l0x.VL53L0X(i2c)
    print("a")
    
    time.sleep(0.5)
    sensor.set_address(0x50+index)
    print("b")
    
    time.sleep(0.1)
    sensor.measurement_timing_budget = 400000
    print("c")
    
    time.sleep(0.3)
    sensor.start_continuous()
    
    sensors.insert(index, sensor)
    print(sensors)

cnt = int()

calibration = []

for i in sensors:
    calibration.append(i.range/10)

while True:
    s = str()
    try:
        for index, i in enumerate(sensors):
            time.sleep(0.05)
            s += str(abs(round(i.range/10 - calibration[index], 1))) + ", "
        cnt += 1
        print(s, cnt)
    except OSError:
        print(OSError)