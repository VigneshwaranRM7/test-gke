from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "gke", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}
