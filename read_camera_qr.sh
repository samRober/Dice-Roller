#! /usr/bin/bash
python3 take_pircutre.py $1
source /home/SamRober/.venv/bin/activate
python3 qr_read.py $1
deactivate