
from threading import Thread
import cv2

class WebcamVideoStream:

       def __init__(self, src=0):
           # initialize the video camera stream and read the first frame
           # from the stream
           print("init")
           self.stream = cv2.VideoCapture(src)
           (self.grabbed, self.frame) = self.stream.read()

           # initialize the variable used to indicate if the thread should
           # be stopped
           self.stopped = False


       def start(self):
           print("start thread")
           # start the thread to read frames from the video stream
           t = Thread(target=self.update, args=())
           t.daemon = True
           t.start()
           return self

       def update(self):
           print("read")
           # keep looping infinitely until the thread is stopped
           while True:
               # if the thread indicator variable is set, stop the thread
               if self.stopped:
                   return


               # otherwise, read the next frame from the stream
               (self.grabbed, self.frame) = self.stream.read()

       def read(self):
           # return the frame most recently read
           return self.frame

       def stop(self):
           # indicate that the thread should be stopped
           self.stopped = True