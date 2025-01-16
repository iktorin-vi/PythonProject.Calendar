from tkinter import Tk, Label
from datetime import datetime
import calendar
import random
from phrases import phrases

colors=["#800000","#D2691E","#000080","#FFFACD","SteelBlue","DarkOliveGreen","#F08080","#FFFF00","#BDB76B","#FF4500","#C71585"]

def random_color_of_window():
    """Change window's color every time when it is opened"""
    return random.choice(colors)

def random_phrase():
    """Generate random phrase"""
    return random.choice(phrases)

def get_calendar():
    """Get date and calendar on month"""
    now = datetime.now()
    year, month, day = now.year, now.month, now.day
    cal_text = calendar.month(year, month)
    date = f"Today: {day:02}.{month:02}.{year}"
    return cal_text, date

root = Tk()
root.minsize(430,160)
root.title("CALENDAR")

root_color=random_color_of_window()
root.configure(bg=root_color)

calendar_text, today_data = get_calendar()

cal_label = Label(root, text=calendar_text, font=("Courier", 20), justify="left")
cal_label.pack()

date_label = Label(root, text=today_data, font=("Arial", 20), fg="black", bg=root_color)
date_label.pack()
phrase_label = Label(root, text=random_phrase(),font=("Courier",14),justify="center",bg=root_color)
phrase_label.pack()
root.mainloop()