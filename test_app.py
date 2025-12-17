from app import detect_deepfake

def test_detect():
    assert detect_deepfake() is not None
