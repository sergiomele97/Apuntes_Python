import time

hour = int(time.strftime("%H"))

if hour >= 19:
    print("Puedes irte a casa")
else:
    print("Quedan", 19-hour, "horas para irte a casa")
