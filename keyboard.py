from pynput.keyboard import Key,Controller

from time import sleep
import time

keyboard: Controller = Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def readmyselection():
    """
    Simulate copying data using the keyboard module.
    """
    try:
        # Simulate pressing Ctrl+C (copy shortcut)
        keyboard.press_and_release('ctrl+c')

        # Wait for a moment (adjust as needed)
        time.sleep(0.1)

        print("Data copied successfully using keyboard shortcut")
    except Exception as e:
        print(f"An error occurred: {e}")
