import pyautogui, time, pyperclip
time.sleep(5)

f = open("data", encoding="utf8")
for line in f:
	pyperclip.copy(line)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press("enter")
