from typing import Optional
from typing_extensions import Literal, TypedDict

class ASGISpecInfo(TypedDict):
    version: str
    spec_version: Optional[Literal['2.0', '2.1']]

class LifespanScope(TypedDict):
    type: Literal[lifespan]
    asgi: ASGISpecInfo

class LifespanReceiveMessage(TypedDict):
    type: Literal[lifespan.startup, lifespan.shutdown]

class LifespanSendMessage(TypedDict):
    type: Literal[lifespan.startup.complete, lifespan.startup.failed, lifespan.shutdown.complete, lifespan.shutdown.failed]
    message: Optional[str]
