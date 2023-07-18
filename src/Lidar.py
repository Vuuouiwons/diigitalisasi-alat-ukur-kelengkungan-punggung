class Lidar:
    def __init__(self, PIN_XSHUT, I2C_ADDRESS):
        self.I2C_ADDRESS = I2C_ADDRESS
        self.PIN_XSHUTw = PIN_XSHUT

    def __repr__(self):
        return f"Lidar-PIN:{self.PIN_XSHUT},ADDRESS:{self.I2C_ADDRESS}"
