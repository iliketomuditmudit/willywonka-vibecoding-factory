# Wonka's Vibe-Coding Factory

A Willy Wonka themed experience where users pick a B2B SaaS idea from a gumball machine, show it to Reachy (or type it in for the MVP), and watch as the factory vibe-codes a working prototype using Claude.

## How It Works

1. **Gumball Machine** — User picks a numbered gumball or types an idea
2. **Golden Ticket Reveal** — The matched idea is shown on a shimmering golden ticket
3. **The Factory** — Oompa Loompas (Claude API) vibe-code a prototype with a candy conveyor belt animation
4. **Result Display** — The generated app is shown in a Wonka-themed browser frame

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Run the server
uvicorn server:app --reload --port 8000
```

Then open http://localhost:8000

## Architecture

```
├── server.py          # FastAPI backend — API routes, Claude integration
├── ideas.py           # 20 B2B SaaS ideas + prompts + fuzzy matcher
├── static/
│   └── index.html     # Willy Wonka themed frontend (single-page app)
├── requirements.txt   # Python dependencies
└── .gitignore
```

### API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/` | Serves the frontend |
| `GET`  | `/api/ideas` | Lists all 20 ideas (for gumball display) |
| `POST` | `/api/match` | Fuzzy-matches typed text to the best idea |
| `POST` | `/api/generate` | Matches idea + generates prototype via Claude |

### Idea Matching

The fuzzy matcher uses keyword overlap scoring — not a simple lookup table. It checks:
- Keyword matches against each idea's keyword list (weighted 3x)
- Partial word matches
- Idea name matches (weighted 10x)
- Slip text word overlap (weighted 2x)

This means users can describe their idea in their own words and it'll find the closest match.

## Integration Points for Reachy

For the full exhibition experience, Alexia's CV pipeline should:
1. Read the idea slip with Reachy's camera (OCR or QR code)
2. POST the extracted text to `/api/match` to confirm the match
3. POST to `/api/generate` to kick off code generation
4. The frontend handles displaying the result

The frontend already supports this — the "Feed to Reachy" flow simulates what the robot would do.

## Team

- **Alexia** — Robot & Computer Vision
- **Mudit** — Ideas & Prompts
- **Kylehu** — API Integration
