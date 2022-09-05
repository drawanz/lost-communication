import uvicorn
from decouple import config

port_from_env = config("PORT")

print(port_from_env)

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=int(port_from_env), reload=True)
