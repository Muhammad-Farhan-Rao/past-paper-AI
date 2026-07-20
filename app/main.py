from fastapi import FastAPI

app = FastAPI(
    title="Past Paper Intelligence Engine",
    description="AI Backend for TARC Solutions",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Past Paper Intelligence Engine",
        "status": "Running Successfully"
    }