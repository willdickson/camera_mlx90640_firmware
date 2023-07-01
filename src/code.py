import time
import board
import busio
import adafruit_mlx90640
from messaging import Messenger

messenger = Messenger()

i2c = busio.I2C(board.SCL1, board.SDA1, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
frame = [0] * 768


while True:

    try:
        mlx.getFrame(frame)
    except ValueError:
        continue

    msg = messenger.update()

    if msg:
        rsp = {'frame': frame}
        messenger.send(rsp)

    elif messenger.error:
        rsp = {
                'time' : time.monotonic(),
                'error': messenger.error_message,
                }
        messenger.send(rsp)


    
    






        







