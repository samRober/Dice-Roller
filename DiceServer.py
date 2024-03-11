from aiohttp import web
import socketio
import read_camera

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)



@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

    
@sio.event
def get_roll(sid, dice_info):
    dice_number = dice_info["number"]
    dice_type = dice_info["type"]
    read_camera.read_camera(read_camera.recognition_type.QR)
    return i

if __name__ == '__main__':
    web.run_app(app)
