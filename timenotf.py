import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! It has been an hour!",
            app_icon=r'C:\Users\DeLL\Dropbox\PROJECTS AND TRIAL CODES\pthon\i.ico',
            app_name='BREAK',
            timeout = 2
                           )
        time.sleep(5) 