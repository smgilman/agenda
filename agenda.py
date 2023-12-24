from tkinter import *
# from tkinter import filedialog
from tkcalendar import Calendar
from datetime import date
import calendar

""" 
Very basic program that allows a user to select a day and add any number of events. Save option will be added
after basic functionality is completed.

author: Sharon Gilman (smgilman)
date created: 12/24/2023
"""

def _display_calendar():
  """ Displays today's month, with the option to cycle through the year's months. """
  today = date.today()
  cal = Calendar(year=today.year, firstweekday="sunday", showweeknumbers=False)
  cal.pack()

def _create_menu(root):
  """ Creates menu at the top of the window. """
  menu_bar = Menu(master=root)
  root.config(menu=menu_bar)
  file_menu = Menu(master=menu_bar)
  file_menu.add_command(label="New Agenda", command=quit)
  # file_menu.add_separator()
  file_menu.add_command(label="Export Agenda", command=quit)
  file_menu.add_separator()
  file_menu.add_command(label="Quit", command=quit)
  menu_bar.add_cascade(label="File", menu=file_menu)

def main():
  root = Tk()
  root.geometry("600x600")
  root.title("Agenda")
  _create_menu(root)
  display_calendar = Button(root, text="Display Calendar", command=_display_calendar)

  display_calendar.pack()
  root.mainloop()

if __name__ == "__main__":
  main()