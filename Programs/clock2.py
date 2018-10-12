from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import calendar
import datetime
import winsound
h = 0
m = 0
s = 0
t = str("AM")
def current_time():
  ##1 Get the total seconds since midnight, January 1, 1970
    total_seconds = calendar.timegm(time.gmtime())
    mili_seconds = total_seconds * 1000
  ##2 Convert mili_seconds to seconds by dividing by 1000
    seconds = mili_seconds//1000
  ##3 Get current second from seconds
    current_second = seconds % 60
  ##4 Get the total minutes by dividing seconds by 60
    minutes = seconds//60
  ##5 Compute current minute from total minute
    current_minute = minutes % 60
  ##6 Obtain total hours by dividing minutes by 60
    hours = minutes//60
  ##7 Get current hour 
    current_hour = hours%24

    
    if current_hour >=12:
      tag = "PM"
    else:
      tag = "AM"
    a =str(h)+":"+str(m)+":"+str(s)+t
    ##Creating and returning our time as a string
    timex = str(current_hour)+":"+str(current_minute)+":"+str(current_second) + tag
    if timex == a:
      beep()
      
    return timex

def beep():
  winsound.Beep(5000,8000)

def alarm(*args):
  global h
  h = int(input("Set the hour"))
  global m 
  m = int(input("Set the minute"))
  global s
  s = int(input("Set the second"))
  global t
  t = str(input("Please enter AM or PM"))
  t = t.upper()

  
  alarm_time = str(h)+":"+str(m)+":"+str(s)+t
  return alarm_time
##Creating a function to exit the goey
def quit(*args):
  root.destroy()
##Creating a function to display time to the goey
def show_time():
  global h
  global m
  global s
  global t
  time = current_time()
  txt.set(time)
  root.after(1000, show_time)
  

root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Black')
root.bind("x", quit)
root.bind("p", alarm)

root.after(1000,show_time)
fnt = font.Font(family='Helvetica', size=60,weight='bold')
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt,font=fnt,foreground="Green",background="Black")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()









  





