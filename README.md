# aiobale (Fork)

This repository is a fork of the original `aiobale` library, maintained specifically for advanced self-bot operations, channel advertising, and experimental Bale flows.

## Vision
The goal of this fork is to iteratively build a complete, bugless, and modern asynchronous library for interacting with the Bale messaging platform. As we encounter new requirements—such as undocumented RPCs, channel commenting, or new message structures—we will implement and test them here. Over time, this will become the most robust open-source library for Bale automation.

### Design Principles for Agents and Humans
- **Patch the Library, Not Just the Bot**: If a feature or fix is foundational to Bale's protocol (e.g., commenting on channels, handling new ChatTypes), implement it in this library rather than patching the end-user bot script.
- **Support Undocumented APIs**: Bale's Web and App clients frequently use undocumented gRPC/WebSocket structures (like `ThreadInfo` / `Alias 8` for channel comments). We aim to reverse-engineer and cleanly integrate these.
- **Graceful Parsing**: Use Pydantic models with forgiving validators to handle unexpected data from Bale's servers without crashing.

## Tools and Scripts

### `scripts/capture_rpc.py`
When attempting to implement a new feature (like reactions, polls, or specific admin actions), you'll often need to know the exact WebSocket payload Bale expects. We provide a Playwright-based script to capture these payloads directly from Bale Web.

**Usage:**
1. Ensure you have playwright installed: `pip install playwright && playwright install chromium`
2. Run the script: `python scripts/capture_rpc.py --out rpc_dump.txt`
3. A visible browser window will open. Log into Bale Web and perform the action you want to reverse-engineer.
4. The exact `[WS SENT]` and `[WS RECV]` protobuf payloads will be printed to the terminal and saved to `rpc_dump.txt`. You can then decode these payloads to understand the required `bale.messaging` method and structure.
