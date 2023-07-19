from dotenv import load_dotenv
import os

def environment(dotEnv=load_dotenv()):
    constants = {
        'client-socket':{
            'port':os.getenv('PORT'),
            'wifi-name':os.getenv('WIFI_NAME'),
            'tello-ip':os.getenv('TELLO_IP'),
        },
        'server-socket-for-video-stream':{
            'vs-udp-ip':os.getenv('VS_UDP_IP'),
            'vs-udp-port':os.getenv('VS_UDP_PORT'),
            'control-udp-port':os.getenv('CONTROL_UDP_PORT'),
            'state-udp-port':os.getenv('STATE_UDP_PORT')
        }
    }
    return constants