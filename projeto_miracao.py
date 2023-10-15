import pyautogui
from time import sleep

# Posição algo - use o mouseInfo
# Fazer algo com essa posição
pyautogui.moveTo(1447,435,duration=2)
for i in range(100):
    sleep(0.5)
    pyautogui.click()