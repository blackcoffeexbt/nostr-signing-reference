import asyncio
import json
import os
from dotenv import load_dotenv
from nostr.key import PrivateKey
from nostr.event import Event, EventKind

# Load Private Key from .env file
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY not found in .env file. Please define it.")

async def run():
    # Initialize Private Key
    private_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))

    # Build an Event
    message = "Message"
    public_key = private_key.public_key.hex()
    event = Event(
        kind=EventKind.TEXT_NOTE,
        content=message,
        public_key=public_key
    )

    # Sign the Event
    print("Signing event with private key:", PRIVATE_KEY)
    private_key.sign_event(event)

    # Output Results
    event_json = event.to_message()
    print("----------------------------------")
    print("Signed Event JSON:", event_json)
    print("Signed event Hash:", event.id)
    print("Signed event signature:", event.signature)
    print("----------------------------------")

if __name__ == "__main__":
    asyncio.run(run())