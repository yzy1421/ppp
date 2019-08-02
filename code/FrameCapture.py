import os
import cv2

def videoname(path):
    name=path.split('.')[0].split('/')[-1]
    #print('videoname:%s'%name)
    return name

# Function to extract frames
def FrameCapture01(path):
    # Path to video file`
    vidObj = cv2.VideoCapture(path)
    #c=1
    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1
    timeF = 100 #the internal of frames
    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        if(count%timeF == 0):
        # Saves the frames with frame-count
            cv2.imwrite("%s_time%d.jpg" % (videoname(path),count), image)

        count += 1
        cv2.waitKey(1)



# Function to put all frames of each video into their own file
def CreateFrameFile(path,finalpath):
    os.chdir(path)
    folder = os.walk(path)
    files = list(folder)[0][2]
    for file in files:
        #file=files[i]
        filepath = path + '/' + file
        filename = file.split('.')[0]
        os.chdir(finalpath)
        #os.mkdir(filename)
        #os.chdir(finalpath + '/' + filename)
        # Driver Code
        if __name__ == '__main__':
            # Calling the function

            FrameCapture01(filepath)
            os.chdir(path)

# path='/home/zy3/Documents/'+'FrameData'
# finalpath='/home/zy3/Documents'
# CreateFrameFile(path,finalpath,1)


# path='/home/zy3/Project_SC'
#
# video_path='/home/zy3/Documents/FINALDATA/VIDS'
#
#
#
# CreateFrameFile(video_path,os.path.join(path,'scene_classification_oringin'),1,3)
print('Successfully Create Files!')

#Function of timeF according to the duration of video
def get_Framenumber(file_path):
    # videoname(path)
    cap = cv2.VideoCapture(file_path)
    if cap.isOpened():

        cap.isOpened()
        rate = cap.get(5)                 #frame rate
        FrameNumber = cap.get(7)          #number of frames
        duration = FrameNumber/rate / 60 #time of video
    return FrameNumber, rate,duration







#path='/home/zy3/Documents/'+'FrameData/20160211_083022_2018-03-20.mp4'
# path='/home/zy3/Documents/FINALDATA/VIDS/20160211_083309_2018-03-27.mp4'
# finalpath='/home/zy3/Documents'
# print(get_Framenumber(path))
# print(get_Framenumber(path1))

path='/home/zy3/Documents/FINALDATA/VIDS'
finalpath='/home/zy3/Project_SC/scene_classification_oringin'
CreateFrameFile(path,finalpath)