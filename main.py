import cv2

def arrowDetection():
    return 0

def getDistance():
    distance =0
    return distance

def moveForward():
    return 0

def moveBackward():
    return 0

def turnLeft():
    return 0

def turnRight():
    return 0

def getColor():
    color = 'red'
    return color

def findContours(img):
    _, threshold = cv2.threshold(img, 
    127, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def dectectShape():
    shape='triange'
    return shape

def linefollwing():
    linefollw = 1

def obstacleDetect():
    turnLeft()

def turnDirection(direction):
    if(direction=='left'):
        turnLeft()
    elif(direction=='right'):
        turnRight()
    elif(direction=='forward'):
        moveForward()
    elif(direction=='backward'):
        moveBackward()