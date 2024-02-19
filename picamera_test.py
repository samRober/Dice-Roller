from picamera2 import Picamera2
import sys
file_name = sys.argv[1]
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)
picam2.controls.AwbEnable = True
picam2.controls.AwbMode = 4
picam2.controls.LensPosition = 11.65276
picam2.start()
#picam2.autofocus_cycle()
picam2.capture_file(file_name)