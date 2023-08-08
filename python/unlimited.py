import pyautogui as p
import time
# time.sleep(4)
# for i in range(10):
limit=input("enter no. of messages:")
msg=input("message you want to send:")
i=0
time.sleep(5)

while i<int(limit):

    p.typewrite(msg)
    p.press('enter')
