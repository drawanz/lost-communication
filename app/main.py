import uvicorn
import os

PORT = os.environ.get("PORT", "8000")

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=PORT, reload=True)