from picamera2 import Picamera2
import sys
from libcamera import controls
import os


def take_picture():
    #set up camera
    os.environ["LIBCAMERA_LOG_LEVELS"] = "3"
    Picamera2.set_logging(Picamera2.ERROR)
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores",format = "BRG888")
    picam2.configure(camera_config)
    picam2.controls.AwbEnable = True
    picam2.controls.AwbMode = 4
    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 7.4,"ExposureTime": 100000, "AnalogueGain": 9.0})


    picam2.start()
    #picam2.autofocus_cycle()
    #print(picam2.capture_metadata()['LensPosition'])
    #picam2.capture_file(file_name)
    return picam2.capture_array()

if __name__ == "__main__":
    file_name = sys.argv[1]
    o =take_picture()