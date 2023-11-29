#! /usr/bin/bash
python3 picamera_test.py $1
source /home/SamRober/.venv/bin/activate
python3 TessTest.py $1
deactivate