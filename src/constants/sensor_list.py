import time
import board
from digitalio import DigitalInOut

# (INDEX, PIN_XSHUT, I2C_ADDRESS)
sensors = [
    (DigitalInOut(board.D4), 0x50),
    (DigitalInOut(board.D17), 0x51),
    (DigitalInOut(board.D27), 0x52),
    (DigitalInOut(board.D22), 0x53),
    (DigitalInOut(board.D10), 0x54),
    (DigitalInOut(board.D9), 0x55),
    (DigitalInOut(board.D21), 0x56),
    (DigitalInOut(board.D5), 0x57),
    (DigitalInOut(board.D6), 0x58),
    (DigitalInOut(board.D13), 0x59),
    (DigitalInOut(board.D19), 0x5a),
    (DigitalInOut(board.D26), 0x5b),
    (DigitalInOut(board.D23), 0x5c),
    (DigitalInOut(board.D24), 0x5d),
    (DigitalInOut(board.D25), 0x5e)
]
