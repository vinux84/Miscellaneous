import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller

def ent():
    gp = keyboard.type('name')
    return gp


ent()












