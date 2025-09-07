from fastapi import FastAPI
from routes import auth
from routes import users, patients, doctors, ailments, prescriptions

# Create the app
app = FastAPI(title="Medical Record API", version="1.0")

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(ailments.router)
app.include_router(prescriptions.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Medical Record API!"}


