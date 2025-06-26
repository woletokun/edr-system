import pytest
from server.models import verify_signature
import hmac, hashlib

def test_signature_valid():
    key = "testkey"
    data = {"foo": "bar"}
    sig = hmac.new(key.encode(), str(data).encode(), hashlib.sha256).hexdigest()
    assert verify_signature(data, sig, key)
