import pyautogui, time, pyperclip
time.sleep(5)

f = open("data", 'r')
for word in f:
	pyperclip.copy(word)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press("enter")