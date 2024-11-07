from fastapi import FastAPI

# Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json")


@app.get("/api/v1/fastapi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}
