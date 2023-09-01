from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/get_phone_number_results")
def results():
    return {"message": "Hello, FastAPI!"}


@app.get("/get_country_code")
def country_code():
    return {"message": "Hello, FastAPI!"}
