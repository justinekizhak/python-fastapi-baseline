from uvicorn.protocols.http.h11_impl import H11Protocol as H11Protocol
from uvicorn.protocols.http.httptools_impl import HttpToolsProtocol as HttpToolsProtocol

AutoHTTPProtocol = H11Protocol
AutoHTTPProtocol = HttpToolsProtocol
