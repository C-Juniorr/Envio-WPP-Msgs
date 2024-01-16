import pywhatkit
import time
import keyboard
from keyboard import press

msg = input('Mensagem que ira enviar!')
j = 0

with open("numeros.txt") as file:
    for line in file:
        print(line)
        time.sleep(8)
        #pywhatkit.sendwhatmsg(line, msg)
        pywhatkit.sendwhatmsg_instantly(line, msg, tab_close=True)
        time.sleep(10)
        j = j+1
        keyboard.press_and_release('ctrl+w')
        time.sleep(6)