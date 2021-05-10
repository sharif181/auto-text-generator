import pyautogui
import time
i = 0
while i<7:
    time.sleep(3)
    pyautogui.typewrite("Enter any text.{}".format((i+1)*10000))
    pyautogui.press('enter')
    i = i+1
