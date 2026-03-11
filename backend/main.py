from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.langgraph_agent import run_agent

from backend.database import engine, SessionLocal
from models import Base, PromptHistory

from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


# CORS middleware (React frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["http://localhost:3000"] for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------- AI Extraction API --------

@app.post("/ai-extract")
def ai_extract(data: dict):

    prompt = data.get("prompt")

    db = SessionLocal()

    try:

        # Save prompt in DB
        new_prompt = PromptHistory(prompt=prompt)
        db.add(new_prompt)
        db.commit()

        # Run AI agent
        result = run_agent(prompt)

        return {"data": result}

    except Exception as e:

        print("ERROR:", e)
        return {"error": "AI processing failed"}

    finally:
        db.close()


# -------- Prompt History API --------

@app.get("/history")
def get_history():

    db = SessionLocal()

    try:

        prompts = db.query(PromptHistory).order_by(
            PromptHistory.created_at.desc()
        ).all()

        return prompts

    finally:
        db.close()