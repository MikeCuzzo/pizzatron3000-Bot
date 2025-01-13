Pizzatron9000-Bot
Pizzatron9000-Bot is an automation script for ordering and customizing pizzas on the New Club Penguin game. The bot interacts with the game window, taking screenshots of orders, reading the text using OCR, and adding various toppings to the pizza based on the order. It uses color-based mouse movements to simulate user actions and add ingredients like cheese, seaweed, shrimp, squid, fish, and hot sauce.

Requirements
To run Pizzatron9000-Bot, you will need:

Python 3.x
Required Python libraries:
pygetwindow
pyautogui
pillow (PIL)
pytesseract
A New Club Penguin window running on your computer
Ensure that you have the necessary permissions to run programs as administrator for interaction with the game.

How to Use
Run VSCode/Program as Administrator: To ensure the bot can interact with the game window properly, open your VSCode or Python program as an administrator.

Open New Club Penguin: Launch New Club Penguin (the game).

Inspect Element in New Club Penguin:

Open Inspect Element in your browser window.
Paste the following script in the Console tab to block ads:
javascript
Copy code
function adblocker() {
document.querySelectorAll("[data-google-query-id]").forEach(e => e.remove())
}
Run the Bot: Execute the Python script (main.py) to begin automating the pizza ordering process. The bot will:

Take screenshots of the current order.
Use OCR (Optical Character Recognition) to extract text and identify the ingredients requested.
Add the corresponding toppings (cheese, seaweed, shrimp, squid, fish) and adjust the hot sauce based on the order.
Example:
bash
Copy code
python main.py
The bot will continue running until it processes 40 orders, adding the appropriate ingredients to each pizza.

Functions
take_order(): Captures an order from the game and processes the ingredients.
add_cheese(), add_seaweed(), add_shrimp(), add_squid(), add_fish(): Simulate adding toppings to the pizza based on the order.
add_sauce(): Adds hot sauce based on the detected text.
find_color_position(): Locates the position of a specified color on the screen.
move_to_color(): Moves the mouse to the detected color on the screen and simulates a click.
main(): Initializes the script and starts the automation process.
Notes
The script uses OCR (pytesseract) to read the order from a screenshot, which means the order text must be clearly visible.
The bot simulates mouse movements and clicks based on the screen's colors, which means the game window must be positioned correctly.
Ensure the correct window title (New Club Penguin) is used to find and interact with the game.
Troubleshooting
"NewCp.exe window not found": This message indicates the bot couldn't find the New Club Penguin window. Make sure the game window is open and properly named.
OCR errors: If the OCR is not reading the text correctly, try adjusting the screenshot region or the quality of the screen resolution.
TODO
Finish the Bot:

Refine the bot’s handling of more diverse orders, ensuring it can interpret additional pizza ingredients.
Implement error handling for unexpected scenarios (e.g., missing or incomplete orders).
Improve the speed and efficiency of the mouse movements to mimic human behavior more accurately.
Add Dessert Mode:

Implement a mode where the bot also prepares and customizes desserts (e.g., cakes, ice cream) based on the order.
Add dessert-related ingredients and interactions to the bot’s behavior.
Ensure that the bot can switch between pizza mode and dessert mode dynamically based on the order.
Disclaimer
Cheating is not condoned. This script is intended for educational purposes only. It is important to respect the terms of service of any platform or game you interact with and use automation tools responsibly. The use of this bot in online environments where cheating is prohibited may result in penalties or bans. Always ensure you are adhering to the rules and guidelines set forth by the respective platform.

License
This project is licensed under the MIT License - see the LICENSE file for details.
