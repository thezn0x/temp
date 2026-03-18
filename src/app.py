from fastapi import FastAPI
from core import *
from models.models import WaitList

app = FastAPI()

@app.get("/")
def root():
    return {
        "name":"SparkDB waitlist API",
        "status":"working"
    }

@app.post("/waitlist")
def waitlist(waitlist:WaitList):
    try:
        value = load_waitlist(waitlist.name, waitlist.email)
        if value:
            return {
                "status": "success",
                "message": "Data uploaded successfully"
            }
        else:
            return {
                "status": "fail",
                "message": "Data not uploaded"
            }
    except Exception as e:
        return {
            "status": "fail",
            "message": str(e)
        }