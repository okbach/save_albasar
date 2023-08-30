
from ScreenCapture import ScreenCapture  



x, y = 0, 0
grabzone = 800


capture = ScreenCapture(x, y, grabzone)



while True:
    screen = capture.get_screen()





