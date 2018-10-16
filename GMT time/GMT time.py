##Logan Douglas
##9/21/18
##Displays current time in GMT

##importing the time and calendar
import time
import calendar


def gm_time():
  while True:
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

    current_time = current_hour,current_minute,current_second
    
  ##8 Print time back to user
    time.sleep(1)
    print("The current time is: ",current_hour,':',current_minute,':',current_second)



gm_time()
