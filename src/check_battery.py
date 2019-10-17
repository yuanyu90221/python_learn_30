from win10toast import ToastNotifier
import psutil

battery = psutil.sensors_battery()
charging = battery.power_plugged
percent = battery.percent
message = '目前電池電量為 ' + str(percent) +'%'
# One-time initialization
toaster = ToastNotifier()
if percent > 40 and not charging:
    print(message)
if percent <= 40 and not charging:
    print('電量不足，請充電'+ message)
elif percent >= 80 and charging:
    toaster.show_toast('電量充足，請拔掉電源線'+message, "alert!", threaded=True, icon_path=None, duration=3)