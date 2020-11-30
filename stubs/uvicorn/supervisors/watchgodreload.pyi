from typing import Any
from uvicorn.supervisors.basereload import BaseReload as BaseReload
from watchgod import DefaultWatcher

logger: Any

class CustomWatcher(DefaultWatcher):
    ignore_dotted_file_regex: str = ...
    ignored: Any = ...
    def __init__(self, root_path: Any) -> None: ...
    def should_watch_file(self, entry: Any): ...

class WatchGodReload(BaseReload):
    reloader_name: str = ...
    watchers: Any = ...
    watch_dir_set: Any = ...
    def __init__(self, config: Any, target: Any, sockets: Any) -> None: ...
    def should_restart(self): ...
