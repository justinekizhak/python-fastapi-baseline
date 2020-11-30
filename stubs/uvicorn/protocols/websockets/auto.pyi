from typing import Any
from uvicorn.protocols.websockets.websockets_impl import WebSocketProtocol as WebSocketProtocol
from uvicorn.protocols.websockets.wsproto_impl import WSProtocol as WSProtocol

AutoWebSocketsProtocol: Any
AutoWebSocketsProtocol = WSProtocol
AutoWebSocketsProtocol = WebSocketProtocol
