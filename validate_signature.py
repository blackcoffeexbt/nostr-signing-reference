import asyncio
import os
import json
from dotenv import load_dotenv
from nostr_sdk import Keys, EventBuilder, NostrSigner, Kind, Timestamp

# Load Private Key from .env file
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY not found in .env file. Please define it.")

def main():
    async def run():
        # Initialize Keys and Signer
        print("Private Key:", PRIVATE_KEY)
        keys = Keys.parse(PRIVATE_KEY)
        signer = NostrSigner.keys(keys)

        # Collect inputs
        kind = int(input("Enter event kind (e.g., 1): "))
        content = input("Enter event content: ")
        timestamp = int(input("Enter event timestamp (unix): "))
        signature = input("Enter signature to validate: ")

        nostr_timestamp = Timestamp.from_secs(timestamp)

        kind_instance = Kind(kind)
        # Build the event with provided details
        builder = EventBuilder(kind_instance, content)
        event = await builder.custom_created_at(nostr_timestamp).sign_with_keys(keys)

        event_json = event.as_json()
        event_obj = json.loads(event_json)
        # Validate the signature
        event_sig  = event_obj['sig']
        is_valid = event_sig == signature
        # print event json
        print("Event JSON:", event_json)
        # print event sig
        print("Event Signature:", event_sig)

        # Output validation result
        print("Validation Result:", "Valid" if is_valid else "Invalid")

    asyncio.run(run())

if __name__ == "__main__":
    main()
