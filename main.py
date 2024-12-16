# Required Libraries
import asyncio
import json
import os
from dotenv import load_dotenv
from nostr_sdk import Keys, EventBuilder, NostrSigner

# Load Private Key from .env file
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY not found in .env file. Please define it.")


def main():
    async def run():
        # Initialize Keys and Signer
        keys = Keys.parse(PRIVATE_KEY)
        signer = NostrSigner.keys(keys)

        # Build an Event
        message = "This is a signed event."
        builder = EventBuilder.text_note(message)

        # Sign the Event
        print("Signing event with private key with hex value:", PRIVATE_KEY)
        event = await builder.sign(signer)
        print("----------------------------------")
        # Output Results
        event_json = event.as_json()
        event_obj = json.loads(event_json)

        print("Signed event Hash:", event_obj['id'])
        print("Signed event signature:", event_obj['sig'])

        # print("Signed Event JSON:", event_json)

        print("----------------------------------")

    asyncio.run(run())


if __name__ == "__main__":
    main()
