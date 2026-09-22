from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from app.core.config import get_settings
from app.core.logging import get_logger
from app.api.v1.router import api_router
from app.core.exceptions import setup_exception_handlers

logger = get_logger(__name__)
settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Mining Digital Twin Backend...")
    yield
    logger.info("Shutting down Mining Digital Twin Backend...")

app = FastAPI(
    title="Mining Digital Twin Backend",
    description="Digital Twin backend for mining and metallurgical operations",
    version=settings.MODEL_VERSION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_exception_handlers(app)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", include_in_schema=False)
def root_redirect():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": settings.MODEL_VERSION}
