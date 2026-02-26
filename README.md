# HelloWorldOA - The Most Overengineered Hello World

## Overview

Welcome to the ultimate overengineering masterclass: a "Hello World" project built with enterprise-grade architecture, comprehensive layering, and complete overkill for what should be a simple greeting service.

> ⚡ **Quick start**
> ```bash
> # install dependencies (uses the custom `uv` CLI - equivalent to `pip install -e .`)
> uv sync
> 
> # run migrations
> alembic upgrade head
> 
> # start the server (via uv)
> ```bash
> uv run uvicorn src.app:app --reload
> ```
> Then visit `http://localhost:8000/docs` for Swagger UI.

## Features

✨ **The Essentials (But More)**
- FastAPI rest API with multiple endpoints
- SQLAlchemy ORM with SQLite database
- Repository pattern for data access
- Service layer for business logic
- Pydantic models for validation
- Alembic migrations for schema management
- Properly named routers and request/response models

## Project Structure

```
hello-world-oa/
├── src/
│   ├── app.py                          # FastAPI application
│   ├── event.py                        # Lifecycle events
│   ├── models/
│   │   ├── base_response.py            # Base response schema
│   │   ├── hello_request.py            # Hello request schema
│   │   ├── world_request.py            # World request schemas
│   │   ├── world.py                    # World models
│   │   └── schemas/
│   │       └── planet.py               # SQLAlchemy Planet model
│   ├── routes/
│   │   ├── base_route.py               # Base route class
│   │   ├── hello.py                    # GET /hello endpoint
│   │   └── world.py                    # World CRUD endpoints
│   ├── services/
│   │   ├── planet_fetcher_service.py   # Fetch planets
│   │   ├── planet_creator_service.py   # Create planets
│   │   ├── planet_updater_service.py   # Update planets
│   │   └── planet_deleter_service.py   # Delete planets
│   └── repositories/
│       └── planet_repo.py              # Database access layer
├── migrations/                         # Alembic migrations
├── main.py                             # Entry point
├── pyproject.toml                      # Dependencies
└── README.md                           # You are here
```

## Endpoints

### Hello Routes
- `GET /hello?receiver=<name>` - Say hello to someone

**Example**:
```bash
curl "http://localhost:8000/hello?receiver=world"
# {"message":"Hello, world!"}
```

(Other endpoints exist for planets; see the routers in `src/routes` for POST/PUT/DELETE payloads.)

## Architecture Layers

### Route Layer
FastAPI routes that handle HTTP requests/responses

### Service Layer
Business logic encapsulation using dependency-injected service classes:
- `PlanetCreatorService` - Create planets
- `PlanetFetcherService` - Read planets
- `PlanetUpdaterService` - Update planets
- `PlanetDeleterService` - Delete planets

### Repository Layer
Data access abstraction using SQLAlchemy:
- `PlanetRepo` - CRUD operations for planets
- `Database` - Session management and context handling

### Model Layer
- Pydantic models for request/response validation
- SQLAlchemy ORM models for database schema

## Database

SQLite database (`helloworld.db`) with Alembic migrations support.

**Tables:**
- `planet` - Stores planet data with timestamps

To run migrations:
```bash
alembic upgrade head
```

## Installation & Setup

1. Install dependencies (this project uses a lightweight `uv` wrapper over pip; you can also run `pip install -e .`):
```bash
uv sync
```

2. Run migrations:
```bash
alembic upgrade head
```

# start the server (using the `uv` CLI which wraps uvicorn)
```bash
uv run uvicorn main:app --reload
```

4. Visit `http://localhost:8000/docs` for Swagger UI

**Conclusion:** Trading simplicity for scalability and enterprise patterns, this is what happens when you treat Hello World like microservices infrastructure. If you think it is unnecessary, then we will probably implement it.

## Technologies

- **FastAPI** - Modern async web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **Alembic** - Database migrations
- **SQLite** - Lightweight database

## Features and future plans
- ✅ Rest API endpoints with **FastAPI**
- ✅ Database migrations with **Alembic**
- ✅ **SOLID**
- ✅ Dependency management with **uv**
- ✅ Typechecking and linting with **ruff** and **ty**
- 100% unit test coverage with **pytest**
- Coverage report generation
- Dockerized build environment
- CI/CD pipeline
- Terraform IAC
- Kubernetes deployment manifests
- API rate limiting
- JWT authentication
- Comprehensive logging infrastructure
- Metrics and monitoring (Prometheus)
- GraphQL endpoint alongside REST
- WebSocket support for real-time updates
- Database connection pooling optimization
- API versioning strategy
- Comprehensive error handling middleware
- Request/response compression
- Performance benchmarking suite
- Redis caching implementation
- Elasticsearch integration
- OpenTelemetry distributed tracing
- Sentry error tracking
- OAuth2/OpenID Connect integration
- Database replication and failover
- Load testing with Locust
- Contract testing for API compatibility
- Celery task queue system
- Message queue (RabbitMQ/Kafka) support
- Multi-environment configuration management
- Secrets management (HashiCorp Vault)
- Health check and readiness probes
- Custom middleware for request tracing
- API gateway integration (Kong/Nginx)
- Database backup and disaster recovery
- Schema versioning and evolution
- Real-time collaboration features
- Webhook event system
- API deprecation handling
- Cost optimization and resource management
- Multi-tenancy support
- Feature flags and gradual rollouts

---

*"I came to say hello. I left as an architect."* 🏗️
