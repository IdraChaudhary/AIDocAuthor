# AI-Assisted Document Authoring Platform (Mock LLM)
This repository is a demo-ready project for the assignment: AI-Assisted Document Authoring and Generation Platform.
Refer to the original assignment spec at: file:///mnt/data/Assignment - 3.pdf

## What is included
- Backend (FastAPI) with JWT auth (demo), project CRUD, mock LLM generation, refinement, DOCX & PPTX export.
- Frontend skeleton (React + Vite) with API client ready to connect.
- Dockerfiles and docker-compose (minimal).

## Quick start (backend)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on http://127.0.0.1:8000

## Export example
- Create a project via POST /projects and then call GET /export/project/<built-in function id>?format=docx

## How to push to GitHub
1. Create a repository on GitHub.
2. In your local project root run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - AI doc platform (mock LLM)"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```
