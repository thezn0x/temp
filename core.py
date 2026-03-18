from logging.handlers import RotatingFileHandler
from znpg import Database
import logging
from dotenv import load_dotenv
import os
import re

# Logger setup
# Initialize Logger
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")

# Setup Stream Handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Setup File Handler
log_file = os.getenv("LOGGING_FILE", "logs.log")
file_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=3)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#----------------

load_dotenv(".env")


db = Database()
db.url_connect(os.getenv("DATABASE_URL"))

def load_waitlist(name:str, email:str):
    try:
        email_match = re.match(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
        if email_match and name:
            with db.transaction() as conn:
                db.insert("waitlist",{
                    "name":name,
                    "email":email
                }, conn=conn)
                logger.info(f"{name} joined waitlist with email {email}")
            return True
        else:
            logger.error(f"[{name}]({email}) failed join to waitlist")
            return False
    except Exception as e:
        logger.error(e)