from plyer import notification
import psutil

battery = psutil.sensors_battery()
charging = battery.power_plugged
percent = battery.percent
message = '目前電池電量為 ' + str(percent) +'%'

if percent > 40 and not charging:
    notification.notify(title='full mode',message=message, app_icon=None, timeout=10)
if percent <= 40 and not charging:
    print('電量不足，請充電'+ message)
elif percent >= 80 and charging:
    notification.notify( title="alert!",message='電量充足，請拔掉電源線'+message, app_icon=None, timeout=10)