from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from utils import html_content
import yfinance as yf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root( q: Union[str, None] = None):
    try:
        data = yf.Ticker(q).history(period='1y')
        return data.to_dict('records')
    except:
        return  HTMLResponse(content=html_content)



