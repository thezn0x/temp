from fastapi import FastAPI
from core import *

app = FastAPI()

@app.post("/waitlist")
def waitlist(name:str, email:str):
    try:
        value = load_waitlist(name, email)
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