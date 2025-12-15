import psutil

def get_info():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    bat = battery.percent if battery else "not available"
    return f"CPU usage {cpu} percent, RAM usage {ram} percent, Battery {bat} percent"
