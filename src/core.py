from znpg import Database
from dotenv import load_dotenv
import os
import re
from utils.logger import get_logger


logger = get_logger("core")
load_dotenv(".env")


db = Database()
db.url_connect(os.getenv("DATABASE_URL"))

def load_waitlist(name:str, email:str):
    try:
        email_match = re.match(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)
        if email_match and name:
            with db.transaction() as conn:
                check = db.select("waitlist", where={"name":name, "email":email}, conn=conn)
                if check:
                    logger.error(f"User [{name}]({email}) already joined waitlist")
                    return False
                db.insert("waitlist",{
                    "name":name,
                    "email":email
                }, conn=conn)
                logger.info(f"[{name}]({email}) joined waitlist successfully")
            return True
        else:
            logger.error(f"[{name}]({email}) failed to join waitlist")
            return False
    except Exception as e:
        logger.error(e)