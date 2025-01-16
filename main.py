import pyautogui
from PIL import ImageGrab
import keyboard
import pygetwindow as gw
import pytesseract


# Helper Functions
def pixel_search(color, region = (0, 0, 1920, 1080)):
    """Searches for a pixel of the given color in the specified screen region."""
    screenshot = ImageGrab.grab(bbox=region)
    pixels = screenshot.load()
    for x in range(region[2] - region[0]):
        for y in range(region[3] - region[1]):
            if pixels[x, y] == color:
                return x + region[0], y + region[1]
    return None

def drag_and_drop(start, end, drop=True):
    """Drags the mouse from start to end."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(end[0], end[1])
    if drop:
        pyautogui.mouseUp()

# Ingredient Functions
def cheese():
    crust = pixel_search((244,203,147),(0,540,1920,1080))
    if crust:
        drag_and_drop((CheeseX,CheeseY),(crust[0]+50,crust[1]+100))

def seaweed(count):
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        if crust:
            drag_and_drop((SeaweedX,SeaweedY),(crust[0]+((i*75)+100),crust[1]))

def shrimp(count):
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        if crust:
            drag_and_drop((ShrimpX,ShrimpY),(crust[0]+((i*100)+100),crust[1]))

def squid(count):
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        if crust:
            drag_and_drop((SquidX,SquidY),(crust[0]+((i*100)+100),crust[1]))

def fish(count):
    for i in range(count):
        crust = pixel_search((244,203,147),(0,540,1920,1080))
        if crust:
            drag_and_drop((FishX,FishY),(crust[0]+((i*100)+100),crust[1]))

def apply_sauce(is_hot):
    if is_hot:
        sauce = pixel_search((255, 225, 0))
    else:
        sauce = pixel_search((255, 77, 0))
    crust = pixel_search((244,203,147),(0,540,1920,1080))
    if crust:
        drag_and_drop(sauce,crust,False)

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
            "supreme pizza": lambda: (cheese(), seaweed(1), shrimp(1), squid(1), fish(1)), 
            "supreme sizzle pizza": lambda: (cheese(), seaweed(1), shrimp(1), squid(1), fish(1)),
            "seaweed-shrimp pizza": lambda: (cheese(), seaweed(2), shrimp(2)),
            "seaweed-squid pizza": lambda: (cheese(), seaweed(2), squid(2)),
            "seaweed fish pizza": lambda: (cheese(), seaweed(2), fish(2)),
            "shrimp squid pizza": lambda: (cheese(), shrimp(2), squid(2)),
            "fish shrimp pizza": lambda: (cheese(), shrimp(2),fish(2)),
            "fish dish": lambda: (cheese(), squid(2), fish(2)),
            "seaweed pizza": lambda: (cheese(), seaweed(5)),
            "shrimp pizza": lambda: (cheese(), shrimp(5)),
            "squid pizza": lambda: (cheese(), squid(5)),
            "fish pizza": lambda: (cheese(), fish(5)),
        }


    for recipie in recipes:
        if recipie in order:
            print("Making", recipie)
            recipes[recipie]()
            break
        else:
            print("No recipie found")
    
    apply_sauce(("hot" or "spicy" or "sizzling" or "flamethrower") in order)



# Game Setup
def set_up():
    print("Setting up game...")
    global CheeseX, CheeseY, SeaweedX, SeaweedY, ShrimpX, ShrimpY, SquidX, SquidY, FishX, FishY

    # Define the screen regions for each ingredient
    ingredient_bar = pixel_search((204,51,51))
    ingredient_bar = (ingredient_bar[0]-300, ingredient_bar[1]-50, ingredient_bar[0] + 500, ingredient_bar[1] + 30)
    test = ImageGrab.grab(bbox=ingredient_bar)
    test.save("test.png")
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