"""
Willy Wonka Vibe-Coding Factory — Backend Server

FastAPI app that:
1. Accepts an idea from the user (typed text or from Reachy's CV)
2. Fuzzy-matches it to one of 20 pre-written prompts
3. Sends the prompt to Claude API to generate a working prototype
4. Returns the generated HTML to the frontend for display
"""

import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import anthropic

from ideas import IDEAS, find_best_match

app = FastAPI(title="Willy Wonka Vibe-Coding Factory")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


class IdeaRequest(BaseModel):
    idea_text: str


class GenerateResponse(BaseModel):
    idea_name: str
    idea_slip: str
    idea_id: int
    generated_html: str


SYSTEM_PROMPT = """You are a brilliant front-end developer who builds stunning single-page web apps.
You ONLY output raw HTML code — a complete, self-contained HTML file with inline CSS and JavaScript.
Do NOT include any markdown, explanations, or code fences. Just the raw HTML starting with <!DOCTYPE html>.
Make the app fully functional, visually polished, and responsive.
Use modern CSS (flexbox, grid, gradients, animations) and vanilla JavaScript.
The app should look production-ready and impressive."""


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.get("/api/ideas")
async def list_ideas():
    """Return all ideas (for the gumball machine UI to show)."""
    return [
        {"id": i["id"], "name": i["name"], "slip_text": i["slip_text"]}
        for i in IDEAS
    ]


@app.post("/api/generate")
async def generate_prototype(request: IdeaRequest):
    """Match an idea and generate a vibe-coded prototype."""
    if not request.idea_text.strip():
        raise HTTPException(status_code=400, detail="Idea text cannot be empty")

    # Fuzzy match to the best idea
    matched_idea = find_best_match(request.idea_text)

    # Call Claude API to generate the prototype
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="ANTHROPIC_API_KEY not set. Please set it as an environment variable.",
        )

    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": matched_idea["prompt"]}
            ],
        )

        generated_html = message.content[0].text

        # Strip markdown code fences if the model included them
        if generated_html.startswith("```"):
            lines = generated_html.split("\n")
            # Remove first line (```html) and last line (```)
            if lines[-1].strip() == "```":
                lines = lines[1:-1]
            else:
                lines = lines[1:]
            generated_html = "\n".join(lines)

        return GenerateResponse(
            idea_name=matched_idea["name"],
            idea_slip=matched_idea["slip_text"],
            idea_id=matched_idea["id"],
            generated_html=generated_html,
        )

    except anthropic.APIError as e:
        raise HTTPException(status_code=502, detail=f"Claude API error: {str(e)}")


@app.post("/api/match")
async def match_idea(request: IdeaRequest):
    """Just match an idea without generating code (for preview)."""
    if not request.idea_text.strip():
        raise HTTPException(status_code=400, detail="Idea text cannot be empty")

    matched = find_best_match(request.idea_text)
    return {
        "id": matched["id"],
        "name": matched["name"],
        "slip_text": matched["slip_text"],
    }
