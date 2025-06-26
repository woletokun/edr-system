# server/models.py
import hmac, hashlib

def validate_event(data: dict) -> bool:
    return isinstance(data.get("hostname"), str) and isinstance(data.get("processes"), list)

def verify_signature(data: dict, signature: str, key: str) -> bool:
    """
    Ensure payload authenticity using HMAC-SHA256.
    """
    digest = hmac.new(key.encode(), msg=str(data).encode(), digestmod=hashlib.sha256).hexdigest()
    return hmac.compare_digest(digest, signature)
