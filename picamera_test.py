from picamera2 import Picamera2
import sys
file_name = sys.argv[1]
picam2 = Picamera2()
picam2.start_and_capture_file(str(file_name))