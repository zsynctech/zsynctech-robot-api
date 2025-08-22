from models.instances import ConfigModel
from cachelib import FileSystemCache
from utils import get_local_ip
import json
import os

BASE_DIR = os.path.dirname(__file__)
CONFIG_JSON = os.path.join(BASE_DIR, "config.json")

IP_ADDRESS = get_local_ip()
COMPUTERNAME = os.environ.get("COMPUTERNAME")

CACHE = FileSystemCache(
    cache_dir=os.path.join(BASE_DIR, "cache"),
    default_timeout=0
)

with open(CONFIG_JSON, 'r', encoding="utf8") as file:
    CONFIG = json.load(file)

config = ConfigModel(**CONFIG)

for instance in config.instances:
    CACHE.set(instance.instance_id, instance)
