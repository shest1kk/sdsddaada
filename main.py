from lib2to3.pytree import Base

from sqlalchemy.orm import Session
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CARholdeRRR"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяет всем ориджинам
    allow_credentials=True,
    allow_methods=["*"],  # Позволяет всем методам
    allow_headers=["*"],  # Позволяет всем заголовкам
)

