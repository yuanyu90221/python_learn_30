from plyer import notification
from time import sleep
import psutil

def check_battery(high, low):
    battery = psutil.sensors_battery()
    charging = battery.power_plugged
    percent = battery.percent
    message = '目前電池電量為 ' + str(percent) +'%'
    if percent <= low and not charging:
        print('電量不足，請充電'+ message)
        return {'title':'battery low!', 'message': 'message' + message}
    elif percent >= high and charging:
        print('電量充足，請拔掉電源線'+message)
        return {'title':'battery high!', 'message': '電量充足，請拔掉電源線'+message}
    elif not charging:
        print(message)
        return {'title':'battery info', 'message': message}
    return {'title':'battery info', 'message': message}

while True:
    alert = check_battery(80, 40)
    notification.notify( title=alert['title'],message=alert['message'], app_icon=None, timeout=10)
    sleep(60)