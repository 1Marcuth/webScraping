from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from heroic_race_crawler import crawler

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get('/events/heroic-race/data')
def laps():
    return crawler.getAllLaps()

@api.get('/events/heroic-race/data-test')
def laps():
    return crawler.getAllLaps()