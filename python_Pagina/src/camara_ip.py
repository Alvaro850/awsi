import numpy as np 
import cv2

class camaraip(object):
    def __init__(self):
        self.cap = cv2.VideoCapture("http://192.168.0.35:8080/video") 
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        self.cap = cv2.VideoCapture("http://192.168.0.35:8080/video")
        ret,frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
        
            return frame
        else:
            return None
        
