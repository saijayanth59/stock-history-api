from typing import Union
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from io import BytesIO
from gannpy import test, preprocess_data, combine_data

import yfinance as yf
import pandas as pd

from utils import html_content


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
        return  HTMLResponse(content=html_content)

@app.post("/gann/text-csv")
async def text_csv(
   csvContent: str = Form(...)
):

    df = pd.read_csv(BytesIO(csvContent.encode()))
    result = test(preprocess_data(df))


    df = pd.DataFrame(result)
    df = df[["date", "buy_above", "sell_below", "tradeType", "entry", "entryTime", "exit", "exitTime", "stopLoss", "stopLossTime","level", "buy_target", "sell_target", "S1", "S2", "S3", "S4", "S5", "B1", "B2", "B3", "B4", "B5"]]


    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="processed_data")
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=processed_data.xlsx"
        },
    )

@app.post("/gann/combine-csv")
async def combine_csv(
    files: List[UploadFile] = File(...),
):
    try:
        dfs = []
        for file in files:
            dfs.append(pd.read_csv(BytesIO(await file.read())))   
        df = combine_data(dfs)
        processed_data = preprocess_data(combined_df)
        result = test(processed_data)

        result_df = pd.DataFrame(result)
        result_df = result_df[
            [
                "date", "buy_above", "sell_below", "tradeType", "entry", 
                "entryTime", "exit", "exitTime", "stopLoss", "stopLossTime",
                "level", "S1", "S2", "S3", "S4", 
                "S5", "B1", "B2", "B3", "B4", "B5"
            ]
        ]

        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            result_df.to_excel(writer, index=False, sheet_name="processed_data")
        output.seek(0)

        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=processed_data.xlsx"
            },
        )
    except Exception as e:
        return {"error": str(e)}