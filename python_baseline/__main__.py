import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from python_baseline.api import api_v1
from python_baseline.core.config import settings, set_env

from dotenv import load_dotenv

import typer
from loguru import logger

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_DOC}/openapi.json",
    debug=settings.DEBUG,
    version=settings.VERSION,
    docs_url=settings.API_SWAGGER_URL,
    redoc_url=settings.API_DOC,
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_v1.api_router, prefix=settings.API_V1_STR)


@app.get("/", status_code=301)
def redirect_to_api():
    return RedirectResponse(settings.API_DOC, status_code=301)


def load_environment(prod: bool = False):
    set_env("PRODUCTION_ENV", str(prod))
    if prod:
        logger.info("Running in production mode...")
        load_dotenv(".env.production.local", override=True)
        load_dotenv(".env.production", override=True)
    else:
        logger.info("Running in development mode...")
        load_dotenv(".env.development.local", override=True)
        load_dotenv(".env.development", override=True)


def main(prod: bool = False):
    load_environment(prod)
    uvicorn.run(
        "python_baseline.__main__:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
    )


if __name__ == "__main__":
    typer.run(main)
