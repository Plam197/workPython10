import os

if os.path.exists('iotxxx.txt') :
    os.remove('iotxxx.txt')
else :
    print('File not found.... -_-')