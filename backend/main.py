from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import datetime

app = FastAPI()

# Разрешаем доступ с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

leaderboard = []

@app.get("/leaderboard")
def get_leaderboard():
    return sorted(leaderboard, key=lambda x: -x["score"])

@app.post("/submit")
def submit_score(name: str, score: int):
    leaderboard.append({"name": name, "score": score})
    return {"message": "Score submitted"}

@app.on_event("startup")
def wipe_monthly():
    if datetime.datetime.now().day == 1:
        leaderboard.clear()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
