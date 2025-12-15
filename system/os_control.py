import os

def open_app(app_name):
    os.system(f"start {app_name}")

def close_app(app_name):
    os.system(f"taskkill /im {app_name}.exe /f")

def open_settings():
    os.system("start ms-settings:")
