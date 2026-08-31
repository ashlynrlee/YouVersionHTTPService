# tests/test_router.py

import sys

sys.path.insert(0,'Server')

from fastapi.testclient import TestClient
from app import app
from unittest.mock import patch
from errors import InvalidDayError, UpstreamError

client = TestClient(app)


def test_happy_path():
    with patch("votdService.votdGet") as mock_service:
        mock_service.return_value = {
            "day": 195,
            "reference": "Revelation 3:20",
            "text": "Behold, I stand at the door and knock...",
            "version_id": 206
        }

        response = client.get("/votd?day=195&version=206")
        assert response.status_code == 200
        assert response.json()["reference"] == "Revelation 3:20"


def test_invalid_day():
    with patch("votdService.votdGet") as mock_service:
        mock_service.side_effect = InvalidDayError("day must be an integer between 1 and 366")

        response = client.get("/votd?day=0&version=206")
        assert response.status_code == 400
        assert response.json()["error"]["code"] == "INVALID_DAY"

def test_default_day_of_year():
    response = client.get("/votd?version=3034")
    assert response.status_code == 200
        
def test_upstream_failure():
    with patch("votdService.votdGet") as mock_service:
        mock_service.side_effect = UpstreamError("YouVersion down")

        response = client.get("/votd?day=195&version=11")
        assert response.status_code == 502
        assert response.json()["error"]["code"] == "UPSTREAM_FAILURE"
