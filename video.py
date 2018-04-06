
#author: Karim
#date: 03/04/2018

"""
Takes a string argument for filename and split the video into frames, default directory is dataset/videos/filename
requires cv2
Attributes:
    filename: a string indicating which video file, should include extension
    isAnomaly: Anomaly status of the video, true being anomaly

"""
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

class Video(object):

    def __init__(self, filename, isAnomaly, width=320, height=240,**kwargs):
        if filename is None:
            raise ValueError("invalid filename argument")
        self.isAnomaly=isAnomaly
        self.filename = filename
        self.frames=[]
        self.frameCount = 0
        self.width = width
        self.height = height
        self.fileLocation = kwargs.get('fileLocation',"")


        self.__setFrames()



    def __split(self):

        if os.path.exists(self.fileLocation) is False:
            print(self.fileLocation)
            raise ValueError("Video File Not Found ")

        #if os.path.exists('dataset/videos/'+self.filename) is False:
         #   raise ValueError("Video File Not Found")
        videoSource = cv2.VideoCapture(self.fileLocation)
        success,image = videoSource.read() #success is true if file exist, and loads first frame in image
        count = 0
        dir = os.path.splitext("dataset/" + self.filename)[0] #gets the directory location
        if os.path.isdir(dir) is False:
            os.makedirs(dir)
        while success:
            resize_image = cv2.resize(image,(self.width, self.height))
            cv2.imwrite(dir+"/frame%d.jpg" %count,resize_image)
            success, image = videoSource.read()
            count+=1
        print("Read %d Frames" %count)
        return count


    def __setFrames(self):

        """Sets frames from the video.
                Retrieves frames from the video and returns an image array.
                Image size is 240x320
                Before running, video should be in 30FPS.
                Args:
                Returns:

                Raises:
                    ValueError: Video File Not Found.
        """

        dir = os.path.splitext("dataset/" + self.filename)[0]  # gets the directory location
        if os.path.isdir(dir) is False:
            self.__split()
        """
        count = len(os.listdir(dir)) #count list of files inside directory

        imageArr=[]
        for i in range(count):
            image = cv2.imread(dir+"/frame%d.jpg"%i)
            if image is not None:
                imageArr.append(image)

        self.frames=imageArr
        self.frameCount = len(imageArr)
        """
    def getFrames(self):
        return np.array(self.frames)

    def getAnomaly(self):
        return self.isAnomaly

    def getFilename(self):
        return self.filename

    def getFrameCount(self):
        return self.frameCount

    def resize(self, new_width, new_height):
        self.frames = [cv2.resize(frame, (new_width, new_height)) for frame in self.frames]

    def __str__(self):
        return "You are print video object, use one of my methods, My filename is "+self.filename

# if __name__ == "__main__":
#      vid = Video("big_buck_bunny_720p_5mb.mp4",False)
#      arr = vid.getFrames()
#      status = vid.getAnomaly()
#      filename = vid.getFilename()
#      print(len(arr))
#      print(status)
#      print(filename)
#      image = arr[0]
#      plt.imshow(image)
#      plt.show()
