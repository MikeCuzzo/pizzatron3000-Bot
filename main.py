import pyautogui
from PIL import ImageGrab
import keyboard
import pygetwindow as gw
import pytesseract


# Helper Functions
def pixel_search(color, region):
    """Searches for a pixel of the given color in the specified screen region."""
    screenshot = ImageGrab.grab(bbox=region)
    pixels = screenshot.load()
    for x in range(region[2] - region[0]):
        for y in range(region[3] - region[1]):
            if pixels[x, y] == color:
                return x + region[0], y + region[1]
    return None

def drag_and_drop(start, end):
    """Drags the mouse from start to end."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(end[0], end[1])
    pyautogui.mouseUp()

# Ingredient Functions
def cheese():
    crust = pixel_search((244,203,147),(0,540,1920,1080))
    drag_and_drop((CheeseX,CheeseY),(crust[0],crust[1]+100))

def seaweed(count):
    cheese()
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        drag_and_drop((SeaweedX,SeaweedY),(crust[0]+(i*100),crust[1]+(100)))

def shrimp(count):
    cheese()
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        drag_and_drop((ShrimpX,ShrimpY),(crust[0]+(i*100),crust[1]+100))

def squid(count):
    cheese()
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        drag_and_drop((SquidX,SquidY),(crust[0]+(i*100),crust[1]+100))

def fish(count):
    cheese()
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        drag_and_drop((FishX,FishY),(crust[0]+(i*100),crust[1]+100))

# Hotkey Handlers
def on_exit():
    print("Exiting")
    exit()

def on_action():
    screenshot = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    order = pytesseract.image_to_string(screenshot).lower()
    print("order: ", order)

    recipes = {
        "cheese pizza": lambda: cheese(),
        "seaweed pizza": lambda: seaweed(5),
        "shrimp pizza": lambda: shrimp(5),
        "squid pizza": lambda: squid(5),
        "fish pizza": lambda: fish(5)

    }

    for recipie in recipes:
        if recipie in order:
            print("Making", recipie)
            recipes[recipie]()
            break
        else:
            print("No recipie found")


# Game Setup
def set_up():
    print("Setting up game...")
    global CheeseX, CheeseY, SeaweedX, SeaweedY, ShrimpX, ShrimpY, SquidX, SquidY, FishX, FishY

    # Define the screen regions for each ingredient
    ingredient_bar = (640, 540, 1920, 1080)
    CheeseX, CheeseY = pixel_search((255, 255, 204), ingredient_bar)
    print("Cheese: ", CheeseX, CheeseY)
    SeaweedX, SeaweedY = pixel_search((82, 160, 1), ingredient_bar)
    print("Seaweed: ", SeaweedX, SeaweedY)
    ShrimpX, ShrimpY = pixel_search((255, 230, 230), ingredient_bar)
    print("Shrimp: ", ShrimpX, ShrimpY)
    SquidX, SquidY = pixel_search((43, 145, 187), ingredient_bar)
    print("Squid: ", SquidX, SquidY)
    FishX, FishY = pixel_search((153, 153, 153), ingredient_bar)
    print("Fish: ", FishX, FishY)

    print("Game setup complete.")

# On start to make sure the window is open
def init():
    newcp_window = gw.getWindowsWithTitle("New Club Penguin")[0]
    if newcp_window:
        print("NewCp.exe window found.")
        set_up()
        return True
    else:
        print("NewCp.exe window not found.")
        return False


# Keyboard Hooks
if init():
    keyboard.add_hotkey("esc", on_exit)
    keyboard.add_hotkey("shift+q", on_action)
    print("Script is running. Press ESC to exit.")
    keyboard.wait()