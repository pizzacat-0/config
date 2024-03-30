import psutil


battery_status = psutil.sensors_battery()
print(f"  {int(battery_status.percent)}")

