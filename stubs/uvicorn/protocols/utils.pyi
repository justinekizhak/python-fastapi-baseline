from typing import Any

def get_remote_addr(transport: Any): ...
def get_local_addr(transport: Any): ...
def is_ssl(transport: Any): ...
def get_client_addr(scope: Any): ...
def get_path_with_query_string(scope: Any): ...