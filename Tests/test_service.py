# tests/test_service.py
import sys

sys.path.insert(0,'Server')

import datetime
from unittest.mock import patch
from votdService import votdGet
from cache import cache
from errors import InvalidDayError, UpstreamError


def setup_function():
    cache.clear()


def test_cache_behavior():
    cacheKey = (195, 206)
    cache[cacheKey] = {
        "day": 195,
        "reference": "Revelation 3:20",
        "text": "cached text",
        "version_id": 206
    }

    result = votdGet(195, 206)
    assert result["text"] == "cached text"


def test_invalid_day():
    try:
        votdGet(0, 206)
    except InvalidDayError:
        assert True
    else:
        assert False


def test_upstream_calendar_failure():
    with patch("youversionClient.getPassageIdForDay") as mock_calendar:
        mock_calendar.side_effect = Exception("boom")

        try:
            votdGet(195, 11)
        except UpstreamError:
            assert True
        else:
            assert False