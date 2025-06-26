import logging
from server.response import handle_response

def test_handle_response(caplog):
    caplog.set_level(logging.WARNING)
    handle_response({"hostname": "test"}, ["malicious.exe"])
    assert "Detected threat" in caplog.text
