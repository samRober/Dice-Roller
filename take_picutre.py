from picamera2 import Picamera2
import sys
from libcamera import controls
import os

class cam():
    
    def __init__(self):
        #set up camera
        os.environ["LIBCAMERA_LOG_LEVELS"] = "3"
        Picamera2.set_logging(Picamera2.ERROR)
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_still_configuration(main={"size": (1920, 1080),"format": "RGB888"}, lores={"size": (640, 480)}, display="lores")
        self.picam2.configure(camera_config)
        self.picam2.controls.AwbEnable = True
        self.picam2.controls.AwbMode = 4
        self.picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 8.0,"ExposureTime": 25000, "AnalogueGain": 10.0})

    def take_picture(self):
        
        self.picam2.start()
        #picam2.autofocus_cycle()
        #print(picam2.capture_metadata()['LensPosition'])
        #picam2.capture_file(file_name)
        output = self.picam2.capture_array("main")
        self.picam2.stop()
        return output

if __name__ == "__main__":
    file_name = sys.argv[1]
    c = cam()
    o =c.take_picture()