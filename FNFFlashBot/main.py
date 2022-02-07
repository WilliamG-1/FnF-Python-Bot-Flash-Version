import time
import pyautogui
import multiprocessing


# Colors
# Left 194,75,153
# Up = 19,250,5
# Down = 1, 255, 255
# Right = 249, 57, 63

def left_arrow():
    x1, x2 = 1335, 1417
    arrowRegionL = pyautogui.screenshot(region=(x1, 350, 85, 85))
    return arrowRegionL

def right_arrow():
    x1, x2 = 1677, 1746
    arrowRegionR = pyautogui.screenshot(region=(x1, 350, 85, 85))
    return arrowRegionR

def up_arrow():
    x1, x2 = 1560, 1632
    arrowRegionU = pyautogui.screenshot(region=(x1, 383, 85, 85))
    return arrowRegionU

def down_arrow():
    x1, x2 = 1446, 1527
    arrowRegionD = pyautogui.screenshot(region=(x1, 383, 85, 85))
    return arrowRegionD


# rightImg = right_arrow()
# upImg = up_arrow()
# downImg = down_arrow()


time.sleep(3)

def left():
    while True:
        leftImg = left_arrow()
        width, height = leftImg.size
        try:
            for i in range(0,width):
                r,g,b = leftImg.getpixel((i, 63))


                if r == 194 and g == 75 and b == 153:
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('left')
                    print('left key pressed')

                    break

        except OSError as e:
            print('OSError')

def down():
    while True:
        downImg = down_arrow()
        width, height = downImg.size
        try:
            for i in range(0,width):
                r,g,b = downImg.getpixel((i, 63))


                if r == 0 and g == 255 and b == 255:

                    pyautogui.keyDown('down')
                    pyautogui.keyUp('down')
                    print('Down key pressed')

                    break


        except OSError as e:
            print('OSError')

def up():
    while True:
        upImg = up_arrow()
        width, height = upImg.size
        try:
            for i in range(0,width):

                r,g,b = upImg.getpixel((i, 63))

                if r == 18 and g == 250 and b == 5:
                    pyautogui.keyDown('up')
                    pyautogui.keyUp('up')
                    print('Up key pressed')

                    break


        except OSError as e:
            print('OSError')

def right():

    while True:
        rightImg = right_arrow()
        width, height = rightImg.size
        try:
            for i in range(0,width):
                r,g,b = rightImg.getpixel((i, 63))

                if r == 249 and g == 57 and b == 63:
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('right')
                    print('Right key pressed')
                    break

        except OSError as e:
            print('OSError')

p1 = multiprocessing.Process(target=left)
p2 = multiprocessing.Process(target=down)
p3 = multiprocessing.Process(target=up)
p4 = multiprocessing.Process(target=right)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()