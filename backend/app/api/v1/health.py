from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings
from app.dependencies.services import AppServices, get_services
from app.schemas.health import HealthResponse, ReadyResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.app_env,
    )


@router.get("/ready", response_model=ReadyResponse)
async def ready(_: AppServices = Depends(get_services)) -> ReadyResponse:
    checks = {
        "services_container": "ok",
    }
    return ReadyResponse(status="ready", checks=checks)
