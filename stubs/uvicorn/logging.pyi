import logging
from typing import Any, Optional

TRACE_LOG_LEVEL: int

class ColourizedFormatter(logging.Formatter):
    level_name_colors: Any = ...
    use_colors: Any = ...
    def __init__(self, fmt: Optional[Any] = ..., datefmt: Optional[Any] = ..., style: str = ..., use_colors: Optional[Any] = ...) -> None: ...
    def color_level_name(self, level_name: Any, level_no: Any): ...
    def should_use_colors(self): ...
    def formatMessage(self, record: Any): ...

class DefaultFormatter(ColourizedFormatter):
    def should_use_colors(self): ...

class AccessFormatter(ColourizedFormatter):
    status_code_colours: Any = ...
    def get_client_addr(self, scope: Any): ...
    def get_path(self, scope: Any): ...
    def get_full_path(self, scope: Any): ...
    def get_status_code(self, record: Any): ...
    def formatMessage(self, record: Any): ...