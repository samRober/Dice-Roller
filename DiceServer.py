from aiohttp import web
import socketio
import read_camera
import time
from threading import Thread, Lock

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)
recognition_type = read_camera.recognition_type.COLOUR

cr = read_camera.camera_reader()
results_lock = Lock()
dice_results = ()

@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

    
@sio.event
def get_roll(sid, dice_info):
    dice_number = dice_info["number"]
    #dice_type = dice_info["type"]
    output_list = []
    results_lock.acquire()
    global dice_results
    for i in dice_results:
        output_list.append(i)
    results_lock.release()
    print(output_list)
    return output_list

@sio.event
def set_recognition_type(sid, type):
    global recognition_type
    match type:
        case 'QR code':
            recognition_type = read_camera.recognition_type.QR
        case 'colour':
            recognition_type = read_camera.recognition_type.COLOUR
        case 'colour HSV':
            recognition_type = read_camera.recognition_type.COLOUR_HSV
        case 'number recognition':
            recognition_type = read_camera.recognition_type.TESSERACT

    print('type changed: ' + recognition_type.name)
            
def continuous_recognition():
    while(True):
        results_lock.acquire()
        
        dice_results = cr.read_camera(recognition_type)   
        results_lock.release()
        time.sleep(1)

def run_server():
    web.run_app(app)


if __name__ == '__main__':
    pro = Thread(target = continuous_recognition,daemon=True)
    pro.start()
    run_server()
