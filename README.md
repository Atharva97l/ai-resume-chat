# AI Resume Chat

FastAPI backend that answers questions using the Word resume in `backend/`.
The app loads the document once at startup and includes a link to the candidate's
GitHub profile (`Atharva97l`); it does not fetch GitHub repositories.

## Run locally

1. Install dependencies with `uv sync`.
2. Set `GROQ_API_KEY` in the project-root `.env` file.
3. Start the API with `uv run uvicorn backend.main:app --reload`.
4. Open `http://127.0.0.1:8000/` to use the frontend, or
   `http://127.0.0.1:8000/docs` to try the API endpoints.

The resume document must be named
`backend/Atharva_Kulkarni_Resume_Starter.docx`. The frontend is served from
`frontend/` with its CSS and JavaScript available under `/static/`.
`GET /api/info` returns API information and the GitHub profile link;
`POST /chat` accepts a JSON body such as
`{"question": "What projects has the candidate worked on?"}`.

Replace placeholder fields in the Word resume (such as phone, email, and
college) with accurate details before sharing or deploying the app.