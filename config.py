# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "20475714"))
API_HASH = os.environ.get("API_HASH", "a3d6d3f2a3d9677d3a581f7364989f4c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5785944181:AAHlWal6DCZX6qMQ0J0CudlrlLDhUiOFmxs")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5747888765")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "luckyhdhdhdsk")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Luckysingh:lucky847428@cluster0.g7zg8gv.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5747888765")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001859282053")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Newmoviesandwebseriesdiscussion2") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
