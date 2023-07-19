import logging
import socket
import time
from threading import Thread
from typing import Optional, Union, Type, Dict

import cv2
from .enforce_types import enforce_types

@enforce_types
class Tello():
    
    # Set up logger
    HANDLER = logging.StreamHandler()
    FORMATTER = logging.Formatter('[%(levelname)s] %(filename)s - %(lineno)d - %(message)s')
    HANDLER.setFormatter(FORMATTER)
    LOGGER = logging.getLogger('djitellopy')
    LOGGER.addHandler(HANDLER)
    LOGGER.setLevel(logging.INFO)
    # Use Tello.LOGGER.setLevel(logging.<LEVEL>) in YOUR CODE
    # to only receive logs of the desired level and higher