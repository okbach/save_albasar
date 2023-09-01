import numpy as np
import threading
from mss import mss
from PIL import Image
import time


class ScreenCapture:
    ''' def __init__(self, x, y, grabzone):
        self.x, self.y, self.grabzone = x, y, grabzone
        self.screen = np.zeros((grabzone, grabzone, 3), np.uint8)
        self.pillow = None
        self.lock = threading.Lock()
        self.frame_count = 0
        self.start_time = time.time()
        self.start()

    def start(self):
        thread = threading.Thread(target=self.update, daemon=True)
        thread.start()

    def update(self):
        while True:
            with mss() as sct, self.lock:
                monitor = {"top": self.y, "left": self.x, "width": self.grabzone, "height": self.grabzone}
                self.pillow = sct.grab(monitor)
                #img = self.pillow
                #mode = img.mode
                #print("Color Mode: RGB")

                self.screen = np.array(self.pillow)
                #print(self.screen.shape)
                self.frame_count += 1
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= 1:
                    fps = self.frame_count / elapsed_time
                    print(f" FPS: {fps:.2f}", end="\r")
                    self.frame_count = 0
                    self.start_time = time.time()'''
    def __init__(self):
        self.screen = None
        self.pillow = None
        self.lock = threading.Lock()
        self.frame_count = 0
        self.start_time = time.time()
        self.start()

    def start(self):
        thread = threading.Thread(target=self.update, daemon=True)
        thread.start()

    def update(self):
        while True:
            with mss() as sct, self.lock:
                monitor = sct.monitors[0]
                monitor_width = monitor["width"]
                monitor_height = monitor["height"]
                # full monitor 
                monitor = {"top": 0, "left": 0, "width": monitor_width, "height": monitor_height}
                self.pillow = sct.grab(monitor)

                self.screen = np.array(self.pillow)

                self.frame_count += 1
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= 1:
                    fps = self.frame_count / elapsed_time
                    print(f" FPS: {fps:.2f}", end="\r")
                    self.frame_count = 0
                    self.start_time = time.time()

    # return np.array
    def get_screen(self):
        with self.lock:
            return self.screen
    # return pillow opject
    def get_pillow(self):
        with self.lock:
            if self.pillow is not None:
                return self.pillow
            else:
                # pillow empty
                return Image.new("RGB", (self.grabzone, self.grabzone))
            
    def get_actual_screen_dimensions(self):
        with mss() as sct:
            screen_info = sct.monitors[0]
            screen_width = screen_info["width"]
            screen_height = screen_info["height"]
        return screen_width, screen_height        

    '''def get_pillow(self):
        with self.lock:
            #return self.pillow
            #return Image.frombytes("RGB", self.pillow.size, self.pillow.bgra, "raw", "BGRX") self.x
            return Image.frombytes("RGB", self.pillow.size, self.pillow.bgra, "raw", "BGRX")  '''





