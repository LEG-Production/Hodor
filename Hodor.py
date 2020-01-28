import pynput 
import time
import threading
from pynput.keyboard import Key, Controller

dummiecheck = input("Hold the door? ")

keyboard = Controller()
count = 1


print ("\n\tHolding the door open...")
while count > 0:
        print("Hodor\n\n")
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        keyboard.press(Key.num_lock)
        keyboard.release(Key.num_lock)
        print("\n\n")
        time.sleep(5)
        count += 1



