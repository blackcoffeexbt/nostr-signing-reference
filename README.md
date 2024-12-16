# Nostr Event Signing Reference

This project serves as a reference for signing a Nostr event using a specified private key. The application outputs the event hash (ID) and the signed hash (sig) to the CLI. It also includes functionality to validate an existing signature.

## Features
- Sign a Nostr event using a provided private key.
- Validate a Nostr event signature.
- Outputs the event hash (ID) and the signature (sig).
- Displays the signed event JSON.

## Prerequisites
- Python 3.10 or higher.
- `venv` for managing a virtual environment.

## Setup Instructions

1. Copy .env.example to .env:
   ```bash
   cp .env.example .env
   ```
   Update the `PRIVATE_KEY` value with your private key hex value if needed.
   
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

1. Activate the virtual environment:
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Signing an Event

Run the signing script:
```bash
python sign_event.py
```

### Validating a Signature

Run the validation script:
```bash
python validate_signature.py
```

Provide the required inputs when prompted:
- **Kind**: Event kind (e.g., `1` for a text note).
- **Content**: Event content.
- **Timestamp**: Unix timestamp of the event.
- **Signature**: Signature to validate.

## Output Example

### Signing Script
When executed, the application outputs:

1. **Event Hash (ID):** A unique identifier for the event.
2. **Event Signature (sig):** The signature generated for the event.

Example:
```plaintext
Signing event with private key with hex value: 8cd4c283c95d1ea1cb8a3bd0169bf0c3e8b42372b0a3cd9318a6085b49d2d8a2
----------------------------------
Signed event hash: 0d38bf4edf790cd44e51a9c40dda2a2ea9274b53e951d9ce99fd9d0610e8135d
Signed event signature: 8f2428426a8bcbdaff78df9bfb1a0d46902e6fcbf2a99af293fc6411f592cfab698f2141fde82914fbe933c1a07ddd2d867e8d08e11b4eba8c7dd6de6ff1de54
----------------------------------
```

### Validation Script
When executed, the validation script outputs:

- **Validation Result:** Indicates whether the signature is valid or not.

Example:
```plaintext
Validation Result: Valid
```