from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import hazard_analyzernew  # your analysis module
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

chat_history = []

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "chat_history": chat_history})

@app.post("/chat")
async def post_chat(request: Request, user_message: str = Form(...)):
    # Add user message to history
    chat_history.append({"role": "user", "content": user_message})

    # Get structured bot analysis
    result_text = hazard_analyzernew.analyze_hazard(user_message)
    hazard_analyzernew.save_results_to_csv(result_text)

    try:
        structured_data = json.loads(result_text)
    except Exception:
        # fallback: show raw response
        structured_data = {"Raw Response": result_text}

    # Store entire structured analysis (dict) in chat_history
    chat_history.append({"role": "bot", "content": structured_data})

    return templates.TemplateResponse("chat.html", {"request": request, "chat_history": chat_history})
