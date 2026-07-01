from dataclasses import dataclass


@dataclass(frozen=True)
class AppServices:
    """
    DI-ready service container.
    Extend this container with db/storage/cache/ai services in upcoming modules.
    """


def get_services() -> AppServices:
    return AppServices()
