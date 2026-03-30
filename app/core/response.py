from typing import Any


def json_response(status_code: int, message: str, data: Any = None) -> dict[str, Any]:
    return {"status_code": status_code, "message": message, "data": data}
