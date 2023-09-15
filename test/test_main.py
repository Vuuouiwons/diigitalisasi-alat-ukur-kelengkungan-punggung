# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Example of how to use the adafruit_vl53l0x library to change the assigned address of
multiple VL53L0X sensors on the same I2C bus. This example only focuses on 2 VL53L0X
sensors, but can be modified for more. BE AWARE: a multitude of sensors may require
more current than the on-board 3V regulator can output (typical current consumption during
active range readings is about 19 mA per sensor).
"""
import time
import board
from digitalio import DigitalInOut
import adafruit_vl53l0x

# declare the singleton variable for the default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
#= board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# declare the digital output pins connected to the "SHDN" pin on each VL53L0X sensor
xshut = [
    DigitalInOut(board.D4),
    DigitalInOut(board.D17),
    DigitalInOut(board.D27),
    DigitalInOut(board.D22),
    DigitalInOut(board.D10),
    DigitalInOut(board.D9),
    DigitalInOut(board.D11),
    DigitalInOut(board.D5),
    DigitalInOut(board.D6),
    DigitalInOut(board.D13),
    DigitalInOut(board.D19),
    DigitalInOut(board.D26),
    DigitalInOut(board.D23),
    DigitalInOut(board.D24),
    DigitalInOut(board.D25) # add more VL53L0X sensors by defining their SHDN pins here
]

for i, power_pin in enumerate(xshut):
    power_pin.switch_to_output(value=False)
    power_pin.value = False
    # These pins are active when Low, meaning:
    #   if the output signal is LOW, then the VL53L0X sensor is off.
    #   if the output signal is HIGH, then the VL53L0X sensor is on.
    print(i, power_pin)
vl53 = []
print(vl53)

for i, power_pin in enumerate(xshut):
    power_pin.value = True
    vl53.insert(i, adafruit_vl53l0x.VL53L0X(i2c))
    print(vl53)
    if i < len(xshut):
        vl53[i].set_address(int(i) + 0x31 + 2)


def detect_range(count=5):
    """take count=5 samples"""
    while count:
        for index, sensor in enumerate(vl53):
            print("Sensor {} Range: {}mm".format(index + 1, sensor.range))
        time.sleep(1.0)
        count -= 1


print(
    "Multiple VL53L0X sensors' addresses are assigned properly\n"
    "execute detect_range() to read each sensors range readings"
)