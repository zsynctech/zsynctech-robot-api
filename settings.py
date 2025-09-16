from dotenv import load_dotenv
from appdirs import AppDirs
import os

load_dotenv()

RABBITMQ_URL = os.environ.get("RABBITMQ_URL")
TOKENS = os.environ.get("TOKENS", None)

APPS_DIR = AppDirs()
SDK_DIR = os.path.join(APPS_DIR.user_data_dir, "zsynctech")
os.makedirs(SDK_DIR, exist_ok=True)
