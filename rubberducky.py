from keyboard import press_and_release, write
from time import sleep

press_and_release("left windows + d")
sleep(0.5)
press_and_release("left windows")
sleep(0.5)
write("chrome")
sleep(0.5)
press_and_release("enter")
sleep(2)
write("https://www.youtube.com/channel/UCjjE0_GDJUyZCR5Ggt2JzqA")
sleep(0.5)
press_and_release("enter")