"""Chapter 28: bounded, validated tool router.

The router never allows the model to authorize itself. A trusted application policy decides
which tools a caller may use. This example is deterministic so its safety boundary is visible.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolCall:
    name: str
    arguments: dict[str, Any]


class AuthorizationError(Exception):
    pass


def get_order_status(order_id: str) -> dict[str, str]:
    if not order_id.startswith("ORD-"):
        raise ValueError("order_id must start with ORD-")
    return {"order_id": order_id, "status": "processing"}


def cancel_order(order_id: str, confirmed: bool = False) -> dict[str, str]:
    if not confirmed:
        raise ValueError("explicit confirmation is required")
    if not order_id.startswith("ORD-"):
        raise ValueError("order_id must start with ORD-")
    return {"order_id": order_id, "status": "cancellation_requested"}


TOOLS: dict[str, Callable[..., dict[str, str]]] = {
    "get_order_status": get_order_status,
    "cancel_order": cancel_order,
}

ROLE_ALLOWLIST = {
    "viewer": {"get_order_status"},
    "support": {"get_order_status", "cancel_order"},
}


def execute(call: ToolCall, role: str) -> dict[str, str]:
    allowed = ROLE_ALLOWLIST.get(role, set())
    if call.name not in allowed:
        raise AuthorizationError(f"role={role!r} may not call {call.name!r}")
    if call.name not in TOOLS:
        raise ValueError("unknown tool")
    return TOOLS[call.name](**call.arguments)


def main() -> None:
    print(execute(ToolCall("get_order_status", {"order_id": "ORD-1001"}), role="viewer"))
    try:
        print(
            execute(
                ToolCall("cancel_order", {"order_id": "ORD-1001", "confirmed": True}),
                role="viewer",
            )
        )
    except AuthorizationError as exc:
        print("blocked as expected:", exc)
    print(
        execute(
            ToolCall("cancel_order", {"order_id": "ORD-1001", "confirmed": True}),
            role="support",
        )
    )


if __name__ == "__main__":
    main()
