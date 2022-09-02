from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from server.routes.lost_routes import router as LostRouter


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(LostRouter, tags=["Lost"], prefix="/lost")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Softfocus Lost Communication"}
