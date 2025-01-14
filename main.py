from tkinter import Tk, Label
from datetime import datetime
import calendar

def get_calendar():
    now = datetime.now()
    year, month, day = now.year, now.month, now.day
    cal_text = calendar.month(year, month)
    today_data = f"Today: {day:02}.{month:02}.{year}"
    return cal_text, today_data

root = Tk()
root.title("CALENDAR")
root.configure(bg="#6495ED")
calendar_text, today_data = get_calendar()

cal_label = Label(root, text=calendar_text, font=("Courier", 12), justify="left")
cal_label.pack()

date_label = Label(root, text=today_data, font=("Arial", 14), fg="white", bg="#6495ED")
date_label.pack()

root.mainloop()
