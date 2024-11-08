from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .errors import register_all_errors
from api.auth.routes import auth_router
from api.banks.routes import bank_router
from api.core.db import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    await init_db()

version = "v1"
version_prefix = f"/api/{version}"
app = FastAPI(
    title="Trackr",
    version=version,
    license_info={"name": "MIT License",
                  "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Praveen Phatak",
        "url": "https://github.com/phatakp",
        "email": "praveenphatak@gmail.com",
    },
    docs_url=f"{version_prefix}/docs",
    openapi_url=f"{version_prefix}/openapi.json")

register_all_errors(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "0.0.0.0"],
)

app.include_router(auth_router, prefix=f"{
                   version_prefix}/auth", tags=["auth"])

app.include_router(bank_router, prefix=f"{
                   version_prefix}/banks", tags=["banks"])
