from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
import json
with open('app-details.json', 'r') as file:
    app_details = json.load(file)

app = FastAPI(
    title=app_details["APP_TITLE"],
    version=app_details["APP_VERSION"],
    contact=app_details["DEV_CONTACT"],
    description=app_details["APP_DESCRIPTION"],
    docs_url=app_details["DOCS_URL"]
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify specific origins instead
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, you can specify specific methods instead
    allow_headers=["*"],  # Allows all headers, you can specify specific headers instead
)
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"detail": "The resource you requested was not found"},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
@app.get("/")
async def read_root():
    return {"message":"Welcome to our Application."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=True, host="0.0.0.0", port=8000)