class ToadrException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int,
        reason: str = None,
        headers: dict = None,
        json_response: dict = None,
    ):
        self._message = message
        self._status_code = status_code
        self._reason = reason
        self._headers = headers
        self._json_response = json_response

    @property
    def message(self) -> str:
        """A short description of the exception."""
        return self._message

    @property
    def status_code(self) -> str:
        """The HTTP status code of the response."""
        return self._status_code

    @property
    def reason(self) -> str:
        """The reason of the exception (message from aiohttp.ClientResponseError)."""
        return self._reason

    @property
    def headers(self) -> dict:
        """The headers of the response."""
        return self._headers

    @property
    def json_response(self) -> dict:
        """The JSON response from the request (full JSON error response, if available)."""
        return self._json_response