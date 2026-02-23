from fastapi import FastAPI
from app.routes import report

app = FastAPI(title="Breast Cancer CPS")

@app.get("/")
def health_check():
    return {"message": "Backend running"}

app.include_router(report.router)