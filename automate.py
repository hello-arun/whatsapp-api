import pyautogui
import time
w,h=pyautogui.size()
print(w,h)
# pyautogui.moveTo(100, 100, duration = 0.1)
pyautogui.click(w*14/15, h*0.02)
i=1
for i in range(10):
    print(i)
    pyautogui.click(w*0.5, h*0.90)
    message="Hello "*10
    pyautogui.typewrite(message)
    time.sleep(0.5)
    pyautogui.click(w*24/25, h*0.90)
    i+=1
