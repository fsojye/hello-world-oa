from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import goodbye_route, hello_route, world_route


def get_app() -> FastAPI:
    app = FastAPI(
        # dependencies=[Depends(authorizer)]
    )
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=7200,
    )

    hello_route.include_router(app)
    goodbye_route.include_router(app)
    world_route.include_router(app)

    return app


app = get_app()
