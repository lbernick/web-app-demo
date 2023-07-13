import requests

def test_hits():
    hits_url = 'http://127.0.0.1:5000/hits'
    first = requests.get(hits_url)
    second = requests.get(hits_url)
    assert second.json() - first.json() == 1