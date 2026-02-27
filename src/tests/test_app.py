from fastapi import FastAPI
from fastapi.routing import APIRoute

from app import get_app


class TestApp:
    def test_get_app_returns_fastapi_instance(self):
        app = get_app()

        assert isinstance(app, FastAPI)

    def test_get_app_should_register_expected_routes(self):
        app: FastAPI = get_app()
        api_routes = [
            f"{route.name}: {route.methods.pop()} {route.path}"
            for route in app.routes
            if type(route) is APIRoute
        ]

        assert "create_world: POST /hello" in api_routes
        assert "say_goodbye: DELETE /goodbye" in api_routes
        assert "get_worlds: GET /worlds" in api_routes
        assert "update_world: PUT /worlds" in api_routes
