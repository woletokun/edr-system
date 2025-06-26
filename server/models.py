# server/models.py
import hmac, hashlib

def validate_event(data: dict) -> bool:
    """
    Validates the structure of the incoming event payload.

    Ensures the 'hostname' is a string and 'processes' is a list.

    Args:
        data (dict): The JSON payload from the agent.

    Returns:
        bool: True if valid structure, False otherwise.
    """
    return isinstance(data.get("hostname"), str) and isinstance(data.get("processes"), list)

def verify_signature(data: dict, signature: str, key: str) -> bool:
    """
    Verifies the authenticity of the event using HMAC-SHA256.

    Args:
        data (dict): The unsigned payload.
        signature (str): The HMAC signature to verify.
        key (str): Shared secret key used for HMAC signing.

    Returns:
        bool: True if the signature matches, False otherwise.
    """
    # Generate a SHA256 HMAC digest from the payload using the secret key
    digest = hmac.new(key.encode(), msg=str(data).encode(), digestmod=hashlib.sha256).hexdigest()

    # Use secure comparison to prevent timing attacks
    return hmac.compare_digest(digest, signature)
