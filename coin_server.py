import random
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Coin Flipper")


@mcp.tool()
def flip_a_coin() -> str:
    """Flips a coin and returns Heads or Tails."""
    return random.choice(["Heads", "Tails"])

if __name__ == "__main__":
    mcp.run()
