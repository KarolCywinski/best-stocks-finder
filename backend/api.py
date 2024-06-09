import webscraper
from fastapi import FastAPI, Query, HTTPException, status
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/best-stocks-finder", StaticFiles(directory="../frontend", html = True), name="frontend")

@app.get("/get-possible-time-frames")
def get_possible_time_frames():
    try:
        return webscraper.fetch_possible_time_frames()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                      detail="Internal Server Error (mechanism of fetching possible time frames)")
        
@app.get("/get-best-stocks")
def get_best_stocks(short_sell: bool = Query(..., description='Short sell or long buy'), 
                    time_frame: str = Query(..., description='Time frame')):
    try:
        return webscraper.fetch_best_stocks(short_sell, time_frame)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                      detail="Internal Server Error (mechanism of fetching the best stocks)")