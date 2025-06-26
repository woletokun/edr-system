from server.detection import detect_threat

def test_detect_malicious():
    evt = {"processes": [{"pid":1,"name":"crypto-miner"}]}
    threat, inds = detect_threat(evt)
    assert threat is True
    assert "crypto-miner" in inds
