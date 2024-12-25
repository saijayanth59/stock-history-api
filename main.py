from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
        data = yf.Ticker(q).history(period='1y').reset_index()
        return data.to_dict('records')
    except:
        return {"message":'Invalid ticker symbol'}



