import pygetwindow as gw
from PIL import ImageGrab
import pyautogui
import pytesseract
import random


def take_order():
    screenshot = pyautogui.screenshot(region=(1200, 230, 300, 200))
    screenshot.save("orderscreenshot.png")
    order = pytesseract.image_to_string(screenshot).lower()
    add_cheese()
    if "seaweed" in order:
        add_seaweed(int(order[order.index("seaweed")-2]))
    if "shrimp" in order:
        add_shrimp(int(order[order.index("shrimp")-2]))
    if "squid" in order:
        add_squid(int(order[order.index("squid")-2]))
    if "fish" in order:
        add_fish(int(order[order.index("fish")-2]))
    print(order)
    if "hot" in order:
        add_sauce(True)
    else:
        add_sauce(False)

def add_cheese():
    move_to_color("#E6E6B3")
    pyautogui.mouseDown()
    move_to_color("#F4CB93",region = (0,540,1920,1080))
    pyautogui.mouseUp()

def add_seaweed(count):
    for _ in range(count):
        move_to_color("#52A001",region=(0,550,1920,650),offset=(100*count,-200))
        pyautogui.mouseDown()
        move_to_color("#F4CB93",region = (0,540,1920,1080))
        pyautogui.mouseUp()

def add_shrimp(count):
    for _ in range(count):
        move_to_color("#FFCCCC",region=(0,550,1920,650),offset=(100,-100))
        pyautogui.mouseDown()
        move_to_color("#F4CB93",region = (0,540,1920,1080))
        pyautogui.mouseUp()

def add_squid(count):
    for _ in range(count):
        move_to_color("#2B91BB",region=(0,550,1920,650),offset=(100,-100))
        pyautogui.mouseDown()
        move_to_color("#F4CB93",region = (0,540,1920,1080))
        pyautogui.mouseUp()

def add_fish(count):
    for _ in range(count):
        move_to_color("#999999",region=(0,550,1920,650),offset=(100,-100))
        pyautogui.mouseDown()
        move_to_color("#F4CB93",region = (0,540,1920,1080))
        pyautogui.mouseUp()
    

def add_sauce(is_hot):
    if is_hot:
        move_to_color("#FF0000")
    else:
        move_to_color("#FF4D00")
    pyautogui.mouseDown()
    while find_color_position("#F4CB93"):
        move_to_color("#F4CB93", offset=(0, -150),region = (0,540,1920,1080))
    pyautogui.mouseUp()


def find_color_position(hex_color, region=None):
    """
    Find the position of the first pixel matching the given hex color on the screen.

    :param hex_color: The hex color to search for (e.g., "#F3CA92").
    :param region: The region to search in (x, y, width, height). Default is the entire screen.
    :return: (x, y) position of the color if found, None otherwise.
    """
    # Convert hex color to RGB
    target_color = tuple(int(hex_color[i:i + 2], 16) for i in (1, 3, 5))
    
    # Capture a screenshot of the specified region
    screenshot = ImageGrab.grab(bbox=region) if region else ImageGrab.grab()
    screenshot.save("fullscreenshot.png")
    if(hex_color == "#52A001"): 
        screenshot.save("ingredientscreenshot.png")
    width, height = screenshot.size
    
    # Search pixel by pixel for the target color
    for x in range(width):
        for y in range(height):
            if screenshot.getpixel((x, y)) == target_color:
                # Adjust coordinates to account for the region
                if region:
                    return x + region[0], y + region[1]
                return x, y
    return None


def move_to_color(hex_color, region=None, offset=(0, 0)):
    """
    Move the mouse to the position of the given hex color if found.

    :param hex_color: The hex color to search for (e.g., "#F3CA92").
    :param region: The region to search in (x, y, width, height). Default is the entire screen.
    :return: True if the color is found and the mouse is moved, False otherwise.
    """
    position = find_color_position(hex_color, region)
    if position:
        pyautogui.moveTo(position[0]+offset[0], position[1]+offset[1])
        return True
    else:
        print(f"Color {hex_color} not found on screen.")
        return False


def main():
    if init():
        for _ in range(40):
            while find_color_position("#F4CB93") is not None:
                take_order()
    else:
        print("Failed to initialize.")


def init():
    newcp_window = gw.getWindowsWithTitle("New Club Penguin")[0]
    if newcp_window:
        print("NewCp.exe window found.")
        return True
    else:
        print("NewCp.exe window not found.")
        return False


if __name__ == "__main__":
    main()
