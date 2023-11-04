import pyautogui

def fill_days(amount: int):
    for _ in range(amount):
        pyautogui.press("9")
        pyautogui.press("0")
        pyautogui.press("0")
        pyautogui.press("tab")
        pyautogui.press("1")
        pyautogui.press("7")
        pyautogui.press("0")
        pyautogui.press("0")
        pyautogui.press("tab")
        pyautogui.press("tab")

def skip_days(amount: int):
    for _ in range(amount*3):
        pyautogui.press("tab")

def fill_weeks(amount: int):
    for _ in range(amount):
        fill_days(5)
        skip_days(2)

def fill_uni_weeks(amount: int):
    for _ in range(amount):
        skip_days(2)
        fill_days(3)
        skip_days(2)

def clear_days(amount: int):
    for _ in range(amount):
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("tab")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("tab")
        pyautogui.press("tab")
del_days = int(input("Hány napot töröljek? "))
first_days = int(input("Hány nap volt a hó elején? "))
middle_weeks = int(input("Hány egyetemi hét volt a hó közepén? "))
last_days = int(input("Hány nap volt a hó végén? "))

for i in range(5):
    print("A program ", 5-i, " másodperc múlva elindul.")
    pyautogui.sleep(1)

clear_days(del_days)
fill_days(first_days)
if first_days > 0:
    skip_days(2)
fill_uni_weeks(middle_weeks)
fill_days(last_days)