import datetime
import os
import time

# Specify the hour and minute for computer to be suspended
suspend_hour = 21
suspend_minute = 30

# Calculate the scheduled notification time as 5 minutes before the suspension time
notification_hour = suspend_hour
notification_minute = suspend_minute - 5
if notification_minute < 0:
    notification_hour -= 1
    notification_minute += 60

while True:
    # Get the current hour and minute
    current_hour = datetime.datetime.now().hour
    current_minute = datetime.datetime.now().minute
    time.sleep(59)

    # Check if the current time is the scheduled notification time
    if current_hour == notification_hour and current_minute == notification_minute:
        os.system("notify-send '5 minutes left before the computer suspends'")

    # Check if the current time is equal to the scheduled suspend time
    if current_hour == suspend_hour and current_minute == suspend_minute:
        date = datetime.datetime.now().date()
        date_str = date.strftime("%d/%m/%Y")
        with open("suspender.txt", "a") as a:
            a.write(f"suspension at {date_str}")
        os.system("systemctl suspend")
        continue
