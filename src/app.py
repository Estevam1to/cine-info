from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import movie

app = FastAPI(
    title="CineInfo API",
    description="CineInfo API provides movie information using Google's Gemini model.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=5000)
