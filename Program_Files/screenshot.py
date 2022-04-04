# Python program to take 
# screenshots 
import os
import shutil
import numpy as np 
import cv2 
import pyautogui 
from datetime import datetime
  
def click_screenshot(tag):
    # take screenshot using pyautogui 
    image = pyautogui.screenshot() 
       
    # since the pyautogui takes as a  
    # PIL(pillow) and in RGB we need to  
    # convert it to numpy array and BGR  
    # so we can write it to the disk 
    image = cv2.cvtColor(np.array(image), 
                         cv2.COLOR_RGB2BGR) 
       
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #printing current time
    print("Current Time =", current_time)
    
    # writing it to the disk using opencv
    cv2.imwrite("a.jpg",image) 
    
    #changing time format. so, that we can rename file
    current_time = now.strftime("%H_%M_%S")
    time = str(current_time)

    old_name = "a.jpg"
    new_name = time+".jpg"
    #renaming file
    os.rename(old_name, new_name)    

    original = new_name
    target = 'generated-report\\'+new_name
    
    shutil.move(original, target)
click_screenshot("Mouse")
