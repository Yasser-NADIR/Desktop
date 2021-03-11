import time
import winsound
from win10toast import ToastNotifier

def timer(message, minute):
	notification = ToastNotifier()
	notification.show_toast("Alarm", f"Alarm will go off in {minute} minute...")
	time.sleep(minute*60)
	winsound.Beep(frequency=2500, duration=1000)
	notification.show_toast("Alarm", message, duration=50)

if __name__ == '__main__':
	message = "poste du gitHub"
	minute = 1
	timer(message, minute)
