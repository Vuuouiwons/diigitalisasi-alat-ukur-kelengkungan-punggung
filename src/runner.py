from src.constants.sensor_list import sensors
from src.sensor import Lidar


def main():
    # init sensor
    sensor_array = [(index, Lidar(pin, address))
                    for index, (pin, address) in enumerate(sensors)]

    print(sensor_array)
