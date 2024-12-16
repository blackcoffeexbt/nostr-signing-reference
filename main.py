# Required Libraries
import asyncio
import json
import os
from dotenv import load_dotenv
from nostr_sdk import Keys, EventBuilder, NostrSigner, Timestamp, SecretKey

# Load Private Key from .env file
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY not found in .env file. Please define it.")


def main():
    async def run():
        # Initialize Keys and Signer
        # keys = Keys.parse(PRIVATE_KEY)
        # signer = NostrSigner.keys(keys)
        secret_key = SecretKey.from_hex("6b911fd37cdf5c81d4c0adb1ab7fa822ed253ab0ad9aa18d77257c88b29b718e")
        keys = Keys(secret_key)

        # print signer
        # print("Signer:", signer)

        # Build an Event
        message = "Message"
        timestamp = 1734354144
        builder = EventBuilder.text_note(message)
        nostr_timestamp = Timestamp.from_secs(timestamp)

        # Sign the Event
        print("Signing event with private key with hex value:", PRIVATE_KEY)
        event = builder.custom_created_at(nostr_timestamp).sign_with_keys(keys)
        print("----------------------------------")
        # Output Results
        event_json = event.as_json()
        print("Signed Event JSON:", event_json)
        event_obj = json.loads(event_json)

        print("Signed event Hash:", event_obj['id'])
        print("Signed event signature:", event_obj['sig'])

        print("Signed Event JSON:", event_json)

        print("----------------------------------")

    asyncio.run(run())


if __name__ == "__main__":
    main()
