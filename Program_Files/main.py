## testing facial recognition
import face_recognition
import cv2
import numpy as np
from screenshot import click_screenshot
import time
import module as m
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#--------------------------------------------------

    # Variables
COUNTER = 0
TOTAL_BLINKS = 0
CLOSED_EYES_FRAME = 3
cameraID = 0
videoPath = "Video/Your Eyes Independently_Trim5.mp4"
# variables for frame rate.
FRAME_COUNTER = 0
START_TIME = time.time()
FPS = 0

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
f = camera.get(cv2.CAP_PROP_FPS)
width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height, f)
fileName = videoPath.split('/')[1]
name = fileName.split('.')[0]
#print(name)


#-------------------------------------------------


# Load a sample picture and learn how to recognize it.
dutta_image = face_recognition.load_image_file("dutta.jpg")
dutta_face_encoding = face_recognition.face_encodings(dutta_image)[0]

# Load a second sample picture and learn how to recognize it.
rishima_image = face_recognition.load_image_file("rishima.jpg")
rishima_face_encoding = face_recognition.face_encodings(rishima_image)[0]

mamta_image = face_recognition.load_image_file("mamta.jpg")
mamta_face_encoding = face_recognition.face_encodings(mamta_image)[0]

rajneesh_image = face_recognition.load_image_file("rajneesh.jpg")
rajneesh_face_encoding = face_recognition.face_encodings(rajneesh_image)[0]

shefali_image = face_recognition.load_image_file("shefali.jpg")
shefali_face_encoding = face_recognition.face_encodings(shefali_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
     dutta_face_encoding,
     rishima_face_encoding,
     mamta_face_encoding,
     rajneesh_face_encoding,
     shefali_face_encoding
]
known_face_names = [
    "Soumyajit",
    "Rishima",
    "Mamta Madan",
    "Rajneesh",
    "Shefali"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = camera.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)
            if len(face_names) == 2:
                print("Multiple Faces Detected , Clicking screenshot")
                click_screenshot("Cam")
            if len(face_names) == 1:
                if face_names[0] == "Unknown" :
                    print("Unkown Face Detected")
                    click_screenshot("Cam")
    process_this_frame = not process_this_frame


    # Display the results
    #
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        
        
    #---------------------------------------------------------------------------------------------------------------------------
    


#while True:
    FRAME_COUNTER += 1
    # getting frame from camera
    ret, frame = camera.read()
   # if ret == False:
        #break

    # converting frame into Gry image.
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = grayFrame.shape
    circleCenter = (int(width/2), 50)
    # calling the face detector funciton
    image, face = m.faceDetector(frame, grayFrame)
    if face is not None:

        # calling landmarks detector funciton.
        image, PointList = m.faceLandmakDetector(frame, grayFrame, face, False)
        # print(PointList)

        #cv2.putText(frame, f'FPS: {round(FPS,1)}', (460, 20), m.fonts, 0.7, m.YELLOW, 2)
        RightEyePoint = PointList[36:42]
        LeftEyePoint = PointList[42:48]
        leftRatio, topMid, bottomMid = m.blinkDetector(LeftEyePoint)
        rightRatio, rTop, rBottom = m.blinkDetector(RightEyePoint)
        # cv2.circle(image, topMid, 2, m.YELLOW, -1)
        # cv2.circle(image, bottomMid, 2, m.YELLOW, -1)

        blinkRatio = (leftRatio + rightRatio)/2
        #cv2.circle(image, circleCenter, (int(blinkRatio*4.3)), m.CHOCOLATE, -1)
        #cv2.circle(image, circleCenter, (int(blinkRatio*3.2)), m.CYAN, 2)
        #cv2.circle(image, circleCenter, (int(blinkRatio*2)), m.GREEN, 3)

        if blinkRatio > 4:
            COUNTER += 1
            #cv2.putText(image, f'Blink', (70, 50), m.fonts, 0.8, m.LIGHT_BLUE, 2)
            # print("blink")
        else:
            if COUNTER > CLOSED_EYES_FRAME:
                TOTAL_BLINKS += 1
                COUNTER = 0
        #cv2.putText(image, f'Total Blinks: {TOTAL_BLINKS}', (230, 17), m.fonts, 0.5, m.ORANGE, 2)

        for p in LeftEyePoint:
            cv2.circle(image, p, 3, m.MAGENTA, 1)
        for p in RightEyePoint:
            cv2.circle(image, p, 3, m.MAGENTA, 1)
        mask, pos, color = m.EyeTracking(frame, grayFrame, RightEyePoint)
        maskleft, leftPos, leftColor = m.EyeTracking(
            frame, grayFrame, LeftEyePoint)

        # draw background as line where we put text.
        #cv2.line(image, (30, 90), (100, 90), color[0], 30)
        #cv2.line(image, (25, 50), (135, 50), m.WHITE, 30)
        #cv2.line(image, (int(width-150), 50), (int(width-45), 50), m.WHITE, 30)
        #cv2.line(image, (int(width-140), 90), (int(width-60), 90), leftColor[0], 30)

        # writing text on above line
        cv2.putText(image, f'{pos}', (35, 95), m.fonts, 0.6, color[1], 2)
        cv2.putText(image, f'{leftPos}', (int(width-140), 95),
                   m.fonts, 0.6, leftColor[1], 2)
        cv2.putText(image, f'Right Eye', (35, 55), m.fonts, 0.6, m.MAGENTA, 2)
        cv2.putText(image, f'Left Eye', (int(width-145), 55),
                   m.fonts, 0.6, m.MAGENTA, 2)
          
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        if (pos == 'Right' and leftPos == 'Right') or (pos == 'Left' and leftPos == 'Left'):
            print("Warning! You're watching outside the screen") 
    
    #---------------------------------------------------------------------------------------------------------------------------

    # Display the resulting image
    cv2.imshow('Video', frame)
    

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
camera.release()
cv2.destroyAllWindows()

