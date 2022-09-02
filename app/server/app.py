from fastapi import FastAPI


from server.routes.lost_routes import router as LostRouter


app = FastAPI()


app.include_router(LostRouter, tags=["Lost"], prefix="/lost")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Softfocus Lost Communication"}
