import asyncio
import json
import os
import argparse
from playwright.async_api import async_playwright

async def handle_websocket(ws, log_file):
    print(f"\n[WS OPENED]: {ws.url}")
    
    def on_framesent(payload):
        print("\n[WS SENT]:", payload)
        with open(log_file, "a") as f:
            f.write(f"[WS SENT] {repr(payload)}\n")
            
    def on_framereceived(payload):
        with open(log_file, "a") as f:
            f.write(f"[WS RECV] {repr(payload)}\n")
            
    ws.on("framesent", on_framesent)
    ws.on("framereceived", on_framereceived)

async def main():
    parser = argparse.ArgumentParser(description="Capture Bale Web RPC WebSocket payloads.")
    parser.add_argument("--out", default="rpc_dump.txt", help="Output file for the RPC logs")
    args = parser.parse_args()

    log_file = args.out
    
    # Clear previous log
    if os.path.exists(log_file):
        os.remove(log_file)
        
    print(f"Launching browser... (Logs will be saved to {log_file})")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 800, 'height': 800})
        page = await context.new_page()
        
        page.on("websocket", lambda ws: handle_websocket(ws, log_file))
        
        print("Navigating to Bale Web...")
        await page.goto("https://web.bale.ai/", wait_until="domcontentloaded")
        
        print("\n*** ACTION REQUIRED ***")
        print("1. The Bale Web interface is now open.")
        print("2. Please log in with your account.")
        print("3. Perform the action you want to reverse-engineer.")
        print("4. The terminal will print the exact payloads, and they will be appended to the log file.")
        print("5. Close the browser window when done.")
        print("***********************\n")
        
        # Wait until the user closes the browser
        try:
            await page.wait_for_event("close", timeout=0)
        except Exception:
            pass
            
        print("Browser closed. Exiting.")

if __name__ == "__main__":
    asyncio.run(main())
