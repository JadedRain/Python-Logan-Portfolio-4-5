This program imports tkinter *, tkinter ttk, tkinter font, time, calendar, datetime, winsound
I then sets variables for hours minutes and seconds and AM/PM
Then there is a function to get the current time
First you get the total seconds from the calendar import with the time zone GM
Then you go thought and calculate the current time of the day for the GM time zone
Then while in the function you check to see if the current hour and set it to AM or PM depending on what time it is
Then You display the current time and if the time is equal to the alarm it will beep
Then you return time

Then defined the funcion for beep
Using the winsound import we creat a beep at the frequency of 5000, and for a duration of 8 seconds

Then we defined the funciton for the alarm
The values for hous, minutes, seconds, and AM/PM are set
Return all variables as global to the program
Then the fucntions creates the alarm and returns it

Then we define the function to quit
using the tkinter imports we create a function to exit the GUI 

Then we define the function to display the time to the GUI
We get the current time and set it to a variable then we run showtime after ever 1 second using the time and tkinter imports

Then using the tkinter imports we create several variables to so GUI opens  up with the following parameters:
That it is fullscreen
That when you press 'X' it runs the quit function
When you press 'p' it runs and starts the alarm
The screen iteslf is black
Selecting the font as Helvetica, with the size of 60px and bolded
Creats time as a string to be used
Then we get the text and have the foreground for the text be green and the text background to be black
Then we place the lable that we made half way from the top and half way from the center and anchor the point to the center
Then we run the alarm if needed
Then the entire process loops