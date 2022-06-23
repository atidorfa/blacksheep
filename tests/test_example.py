# Testing example: https://fastapi.tiangolo.com/tutorial/testing/
import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient


app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}


client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# Async Tests: https://fastapi.tiangolo.com/advanced/async-tests/
@pytest.mark.asyncio
async def test_async_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
