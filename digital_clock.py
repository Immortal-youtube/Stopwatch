
from time import sleep
from tkinter import *


hours,minutes,seconds,miliseconds = 00,00,00,00

x = True
def stop():
    global x
    print("heard it")
    x = False

def reset():
    global x
    x = False
    global hours,minutes,seconds,miliseconds
    hours,minutes,seconds,miliseconds = 00,00,00,00
    text.config(text="00:00:00")
    

def start():
    global hours,minutes,seconds,miliseconds
    global x
    if x == False:
        x = True
    while x:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        text.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        text.update()
        

window = Tk()
window.title("Stopwatch")
window.resizable(0,0)
window.iconbitmap("clock.ico")
window.configure(bg="black")
text = Label(window, text="00:00:00", font=("Arial", 100), fg="white", bg="black")
text.pack()
startButton = Button(window, text="Start", font=("Arial", 20), fg="white", bg="black",command=lambda: start())
stopButton = Button(window, text="Stop", font=("Arial", 20), fg="white", bg="black",command=lambda: stop())
resetButton = Button(window, text="Reset", font=("Arial", 20), fg="white", bg="black",command=lambda: reset())

if __name__ == "__main__":
    startButton.pack_configure(side="right")
    stopButton.pack_configure(side="left")
    resetButton.pack_configure(side="bottom")
    window.mainloop()