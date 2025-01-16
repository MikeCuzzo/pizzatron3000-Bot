# Pizzatron3000-Bot

## Created by MikeCuzzo: https://mikecuzzo.github.io/

Pizzatron9000-Bot is an automation script for playing the Pizzatron 3000 mini-game New Club Penguin game. The bot interacts with the game window, taking screenshots of orders, reading the text using OCR, and adding various toppings to the pizza based on the order. It uses color-based mouse movements to map and simulate user actions and add ingredients like cheese, sauce, seaweed, shrimp, squid, and fish.

## Requirements

To run Pizzatron3000-Bot, you will need:

- Python 3.x
- Required Python libraries:
  - pygetwindow
  - pyautogui
  - pillow (PIL)
  - pytesseract
- A 'New Club Penguin' window running on your computer

### Ensure that you have the necessary permissions to run programs as an administrator for interaction with the game.

# How to Use

- Run Program as Administrator: To ensure the bot can interact with the game window properly, open your Python program as an administrator.
  If in VSCode, run that as administrator
- Whenever a pizza appears on screen, press `shift+q` to dispense the ingredients. Then add sauce yourself _(will be automated eventually)_

## Recommended: Disable Ads

- Open New Club Penguin: Launch New Club Penguin (the game).
- Inspect Element in New Club Penguin (Ctrl + Shift + I):
- Paste the following script in the Console tab to block ads:

`function adblocker() { 
document.querySelectorAll("[data-google-query-id]").forEach(e => e.remove())
}
setInterval(adblocker, 5000)
`

## Run the Bot: Execute the Python script (main.py) to begin automating the pizza ordering process. The bot will:

- Take screenshots of the current order.
- Use OCR (Optical Character Recognition) to extract text and identify the ingredients requested.
- Add the corresponding toppings (cheese, seaweed, shrimp, squid, fish) and adjust the hot sauce based on the order.
- The bot will continue running until it processes 40 orders, adding the appropriate ingredients to each pizza.

Functions

- Helper Functions

  - `pixel_search(color,region)` takes in a RGB color and a region and returns the X,Y coordinates of the color
  - `drag_and_drop(start,end)`, takes in two sets of coordinates, grabs from the start and drops at the end

- Ingredient functions

  - `cheese(), seaweed(count), shrimp(count), squid(count), fish(count)`
  - All of these functions control which ingredients to select and add to the pizza, and how many

- Hotkey Handlers

  - `on_action()` detects when the user presses `shift+q`, and will proceed to process the current order on the screen
  - `on_exit()` detects when the user presses `esc` which will end the program

- Setup Functions
  - `init()` makes sure the 'New Club Penguin' is open before proceedein to the rest of the program
  - `set_up()` maps out where each ingredient coordinate is for ease of access later

### Notes

- The script uses OCR (pytesseract) to read the order from a screenshot, which means the order text must be clearly visible.
- The bot simulates mouse movements and clicks based on the screen's colors, which means the game window must be positioned correctly.
- Ensure the correct window title (New Club Penguin) is used to find and interact with the game.

### Troubleshooting

- "NewCp.exe window not found": This message indicates the bot couldn't find the New Club Penguin window. Make sure the game window is open and properly named.
  OCR errors: If the OCR is not reading the text correctly, try adjusting the screenshot region or the quality of the screen resolution.

## TODO

- Finish the Bot:

  - Add automatic sauce feature
  - Improve ingredient drop accuracy
  - Impliment more error handling and fail safes, incase of unforseen errors or glitches

- Implement Dessert mode: Same core functionality, but within the dessert mode setting

## Disclaimer

This script is intended for educational purposes only. It is important to respect the terms of service of any platform or game you interact with and use automation tools responsibly. The use of this bot in online environments where cheating is prohibited may result in penalties or bans. Always ensure you are adhering to the rules and guidelines set forth by the respective platform.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
