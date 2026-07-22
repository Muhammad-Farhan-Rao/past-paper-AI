from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Past Paper Intelligence Engine",
    description="AI Backend for TARC Solutions",
    version="1.0.0"
)
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Past Paper Intelligence Engine",
        "status": "Running Successfully"
    }

