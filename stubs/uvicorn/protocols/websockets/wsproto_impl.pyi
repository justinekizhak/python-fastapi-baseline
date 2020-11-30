import asyncio
from typing import Any, Optional
from uvicorn.protocols.utils import get_local_addr as get_local_addr, get_remote_addr as get_remote_addr, is_ssl as is_ssl

class WSProtocol(asyncio.Protocol):
    config: Any = ...
    app: Any = ...
    loop: Any = ...
    logger: Any = ...
    root_path: Any = ...
    connections: Any = ...
    tasks: Any = ...
    transport: Any = ...
    server: Any = ...
    client: Any = ...
    scheme: Any = ...
    connect_event: Any = ...
    queue: Any = ...
    handshake_complete: bool = ...
    close_sent: bool = ...
    conn: Any = ...
    read_paused: bool = ...
    writable: Any = ...
    bytes: bytes = ...
    text: str = ...
    def __init__(self, config: Any, server_state: Any, _loop: Optional[Any] = ...) -> None: ...
    def connection_made(self, transport: Any) -> None: ...
    def connection_lost(self, exc: Any) -> None: ...
    def eof_received(self) -> None: ...
    def data_received(self, data: Any) -> None: ...
    def handle_events(self) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...
    def shutdown(self) -> None: ...
    def on_task_complete(self, task: Any) -> None: ...
    scope: Any = ...
    def handle_connect(self, event: Any) -> None: ...
    def handle_no_connect(self, event: Any) -> None: ...
    def handle_text(self, event: Any) -> None: ...
    def handle_bytes(self, event: Any) -> None: ...
    def handle_close(self, event: Any) -> None: ...
    def handle_ping(self, event: Any) -> None: ...
    def send_500_response(self) -> None: ...
    async def run_asgi(self) -> None: ...
    async def send(self, message: Any) -> None: ...
    async def receive(self): ...
