from fastapi import FastAPI, Path, Query
from typing import List, Optional
from pydantic import BaseModel
from api import courses,sections,users


app = FastAPI()


app.include_router(users.router)

