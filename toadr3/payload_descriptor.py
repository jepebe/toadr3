from .exceptions import SchemaException


class PayloadDescriptor:
    def __init__(self, data: dict):
        if "payloadType" not in data:
            raise SchemaException("Missing 'payloadType' in payload descriptor schema.")

        self._payload_type = data["payloadType"]
        self._units: str | None = data.get("units", None)
        self._currency: str | None = data.get("currency", None)

    @property
    def payload_type(self) -> str:
        """The type of the payload."""
        return self._payload_type

    @property
    def units(self) -> str | None:
        """The measurement units."""
        return self._units

    @property
    def currency(self) -> str | None:
        """Currency of price payload."""
        return self._currency