import pyautogui
import time
import pyperclip

length = 500
total_processed = 0  # Counter for total lines processed

# Sleep for 5 seconds to give you time to prepare
time.sleep(5)

while total_processed < length:
    f = open("data", encoding="utf8")
    
    for line in f:
        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

        total_processed += 1

        if total_processed >= 500:
            break  # Exit the loop when the total count reaches 500
    
    f.close()  # Close the file

input("Press enter to continue...")
