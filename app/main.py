import uvicorn
import os

port_from_env = os.environ.get("PORT")

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=int(port_from_env), reload=True)