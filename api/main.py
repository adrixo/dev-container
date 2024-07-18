from fastapi import FastAPI
import uvicorn

def main():
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        proxy_headers=True,
        loop="asyncio",
        forwarded_allow_ips="*",
    )

def hello():
    print("Hello, world!")

if __name__ == "__main__":
    main()
