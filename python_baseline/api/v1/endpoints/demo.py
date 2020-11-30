from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HelloWorld(BaseModel):
    hello: str


@router.get("/", response_model=HelloWorld)
def get_hello_world() -> Any:
    """
    Hello world
    """
    return {"hello": "world"}

