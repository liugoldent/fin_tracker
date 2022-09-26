from fastapi import FastAPI
from router.stock.index import router as stockRouter

app = FastAPI() # 建立一個 Fast API application
app.include_router(stockRouter,prefix='/stock')

@app.get("/") # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "World"}