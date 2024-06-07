import socketio


@sio.on('connect', namespace='/chat')
def connect_handler(sid, environ):
    print('Connection request')
    if environ['REMOTE_ADDR'] in blacklisted:
        return False  # reject


# as a method:
def message_handler(sid, msg):
    print('Received message: ', msg)
    sio.send(sid, 'response')


socket_io.on('message', namespace='/chat', handler=message_handler)
