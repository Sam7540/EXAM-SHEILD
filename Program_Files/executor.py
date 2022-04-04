from subprocess import *
import time

Popen('python main.py')
time.sleep(1)
Popen('python mp.py')
time.sleep(1)
Popen('python audio.py')
time.sleep(1)
Popen('python quiz.py')
time.sleep(1)
