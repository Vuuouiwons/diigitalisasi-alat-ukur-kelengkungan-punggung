import time
import board
from digitalio import DigitalInOut

# (INDEX, PIN_XSHUT, I2C_ADDRESS)
sensors = [
    (board.D4, "0xF0"),
    (board.D17, "0xF1"),
    (board.D27, "0xF2"),
    (board.D22, "0xF3"),
    (board.D10, "0xF4"),
    (board.D9, "0xF5"),
    (board.D11, "0xF6"),
    (board.D5, "0xF7"),
    (board.D6, "0xF8"),
    (board.D13, "0xF9"),
    (board.D19, "0xFA"),
    (board.D26, "0xFB"),
    (board.D23, "0xFC"),
    (board.D24, "0xFD"),
    (board.D25, "0xFE")
]
