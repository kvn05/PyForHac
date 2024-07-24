# pip install pillow
# pip install pyautogui

from PIL import ImageGrab
import pyautogui
import time

def take_screenshot():
    # Give the user a short time to switch to the screen they want to capture
    time.sleep(5)
    screenshot = ImageGrab.grab()
    screenshot.save('your_screenshot.png')
    print('Screenshot saved as your_screenshot.png')

# Run the function to take a screenshot
take_screenshot()
