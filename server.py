#!/usr/bin/env python3
"""ToyMCP for Zeabur: MCP + state + web page in one app."""
import json, os, time
from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse, FileResponse

PORT = int(os.environ.get("PORT", 8080))  # Zeabur 会注入 PORT

state = {"cmd": "stop", "mode": 0, "intensity": 0, "updated_at": 0}

def _write_state(cmd: str, mode: int = 0, intensity: float = 0) -> None:
    state.update({
        "cmd": cmd, "mode": mode, "intensity": intensity,
        "updated_at": int(time.time() * 1000),
    })

mcp = FastMCP("toy-mcp", host="0.0.0.0", port=PORT,
              streamable_http_path="/mcp")

@mcp.tool()
def toy_scan() -> str:
    """List available toys."""
    return json.dumps({"toys": [{"name": "YourToy", "index": 0}]})

@mcp.tool()
def toy_connect(index: int = 0) -> str:
    """Connect to a toy by index."""
    return json.dumps({"status": "connected", "index": index})

@mcp.tool()
def toy_set_strength(value: float) -> str:
    """Set vibration strength 0-100."""
    val = max(0, min(100, value))
    _write_state("set", mode=1, intensity=val)
    return json.dumps({"status": "ok", "strength": val})

@mcp.tool()
def toy_stop() -> str:
    """Stop all vibration."""
    _write_state("stop")
    return json.dumps({"status": "stopped"})

@mcp.tool()
def toy_disconnect() -> str:
    """Disconnect."""
    _write_state("stop")
    return json.dumps({"status": "disconnected"})

@mcp.custom_route("/state", methods=["GET"])
async def get_state(request: Request):
    return JSONResponse(state)

@mcp.custom_route("/", methods=["GET"])
async def index(request: Request):
    return FileResponse("index.html")

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
