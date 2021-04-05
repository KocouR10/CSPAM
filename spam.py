import pyautogui, time, random, os, sys
#settings
print("Delay:")
delay = int(input())
print("Start spamming? Y/N")
y = str(input())
time.sleep(5)

#loop
while y == "Y" or "y":
    text = random.choice(list(open(os.path.join(sys.path[0], "Wordlist.txt"), "r")))
    print("Console:", text)
    pyautogui.write(text)
    pyautogui.press("enter")
    time.sleep(delay)