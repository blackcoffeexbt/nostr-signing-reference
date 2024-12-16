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

    # Collect inputs
    kind = int(input("Enter event kind (e.g. 1): "))
    content = input("Enter event content: ")
    timestamp = int(input("Enter event timestamp (unix): "))
    signature = input("Enter signature to validate: ")

    # Build an Event
    public_key = private_key.public_key.hex()
    event = Event(
        kind=EventKind(kind),
        content=content,
        created_at=timestamp,
        public_key=public_key
    )

    # Sign the Event
    private_key.sign_event(event)

    # Validate the Signature
    event_sig = event.signature
    is_valid = event_sig == signature

    event_json = event.to_message()

    print("----------------------------------")
    print("Event JSON:", event_json)
    print("Expected Signature:", signature)
    print("Event Signature:   ", event_sig)
    print("Validation Result:", "Valid" if is_valid else "Invalid")
    print("----------------------------------")

if __name__ == "__main__":
    asyncio.run(run())
