import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1400177030:AAHyzE2nYAU0erza0zat22Xxi2_LlzkKhJQ")
API_ID = int(os.environ.get("API_ID", "27197067"))
API_HASH = os.environ.get("API_HASH", "21d4ea03b7653f3ab6779c1b6f542afd")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002117569579"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5026253921").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://nakulagamage123:0MwmsQST6FFmWodR@cluster0.n4tovko.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))