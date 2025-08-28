from appdirs import AppDirs
import os


APPS_DIR = AppDirs()
SDK_DIR = os.path.join(APPS_DIR.user_data_dir, "zsynctech")
os.makedirs(SDK_DIR, exist_ok=True)
