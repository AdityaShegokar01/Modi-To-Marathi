# Modi Marathi Backend (Module 01 - Foundation)

Production-ready FastAPI foundation for the **Modi Lipi → Modern Marathi Translation Platform**.

## Features

- FastAPI app factory
- API v1 routing scaffold
- Typed environment configuration (Pydantic Settings)
- Structured logging (JSON/plain)
- Global exception handling
- Health (`/api/v1/health`) and readiness (`/api/v1/ready`) endpoints
- DI-ready service container
- Unit tests with pytest

## Tech

- Python 3.11+
- FastAPI
- Pydantic v2 + pydantic-settings
- python-json-logger
- pytest

## Setup

### 1. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\\Scripts\\activate   # Windows
```

### 2. Install dependencies

```bash
pip install -e ".[dev]"
```

### 3. Configure environment

```bash
cp .env.example .env
```

### 4. Run server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Run tests

```bash
pytest
```

## Endpoints

- `GET /api/v1/health`
- `GET /api/v1/ready`

## Design Notes

- `app/core/config.py`: all env-driven settings
- `app/core/logging.py`: centralized logging formatter setup
- `app/core/errors.py`: consistent error response contract
- `app/dependencies/services.py`: DI-ready service container for future modules
