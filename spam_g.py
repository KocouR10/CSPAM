import tkinter as tk
import sys, os, time, random
import pyautogui as pag

y_run = "N"

root = tk.Tk()
root.title("Cr1pt1k GUI Spammer")
delay_var = tk.IntVar()
odeslani_var = tk.IntVar()

def run():
    time.sleep(5)
    global y_run
    y_run = "Y"
    print("y_run set to Y")
    print(y_run)
    global p_odeslani
    p_odeslani = odeslani_var.get()
    destroy()

#label
tk.Label(root, text="Delay:").grid(row=0, column=0)
tk.Label(root, text="Pocet odeslani:").grid(row=1, column=0)

#entry
entry = tk.Entry(root, textvariable = delay_var).grid(row=0, column=2)
pocet_odeslani = tk.Entry(root, textvariable = odeslani_var).grid(row=1, column=2)

#button
start = tk.Button(root, text = "Start!", command = run).grid(row=0, column=3)

def destroy():
    root.destroy()

root.mainloop()
odeslano = 1
if y_run == "Y":
    while odeslano < p_odeslani:
        delay = delay_var.get()
        text = str(random.choice(list(open(os.path.join(sys.path[0], "Wordlist.txt"), "r"))))
        pag.write(text)
        pag.press("enter")
        print(odeslano)
        odeslano += 1
        time.sleep(delay)
else:
    print("ERR")