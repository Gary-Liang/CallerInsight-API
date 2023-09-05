from fastapi import FastAPI

app = FastAPI()


# placeholder for database query for phone number inserts 
def recordedData():
    return None
    

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/get_phone_number_results")
def results():
    return {"message": "Hello, FastAPI!"}


@app.get("/get_country_code")
def country_code():
    return {"message": "Hello, FastAPI!"}

@app.get("/authenticate")
def authenticate():
    return {"": ""}

@app.get("/redirect")
def redirect():
    return {"":""}