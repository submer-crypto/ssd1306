import adafruit_framebuf as framebuf
from ..ssd1306 import BASE_SSD1306_I2C


# Implementation based on Adafruit PureIO SMBus interface.
class SSD1306_I2C(BASE_SSD1306_I2C):
    def __init__(
            self,
            width,
            height,
            i2c,
            res=None,
            addr=0x3C,
            external_vcc=False,
            buf_format=framebuf.MVLSB):
        super(width, height, buf_format, i2c, res, addr, external_vcc)

    def write_cmd(self, cmd):
        self.i2c.write_byte_data(self.addr, 0x80, cmd)  # Co=1, D/C#=0

    def write_data(self, buf):
        self.i2c.write_i2c_block_data(self.addr, 0x40, buf)  # Co=0, D/C#=1
