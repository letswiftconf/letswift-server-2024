from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from typing import List

from model import SocialLinks, Sponsor, Organizer, Speaker, Session, FAQ
from data import sponsors, organizers, speakers, sessions, faqs

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Error handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# API endpoints
@app.get("/sponsor", response_model=List[Sponsor])
async def get_sponsors():
    return sponsors

@app.get("/organizer", response_model=List[Organizer])
async def get_organizers():
    return organizers

@app.get("/speaker", response_model=List[Speaker])
async def get_speakers():
    return speakers

@app.get("/schedule", response_model=List[Session])
async def get_schedule():
    return sessions

@app.get("/faq", response_model=List[FAQ])
async def get_faqs():
    return faqs

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
