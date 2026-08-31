from Server.youversionClient import getPassageIdForDay, getPassageText
from Server.cache import cache
from Server.errors import UpstreamError, InvalidDayError


def votdGet(day: int, version: int) -> dict:
    #function that call, forces defualt
    if not isinstance(day, int) or day < 1 or day > 366:
        raise InvalidDayError("day must be an integer between 1 and 366")

    cachekey = (day,version)
    if cachekey in cache:
        return cache[cachekey]
    
    try:
        passageId = getPassageIdForDay(day)
    except Exception as e:
        raise UpstreamError(f"YouVersion calendar API failed: {e}")

    try:
        passage = getPassageText(version, passageId)
    except Exception as e:
        raise UpstreamError(f"YouVersion passage API failed: {e}")

    result = {"day": day, "reference": passage["reference"],"text": passage["content"],"version_id": version }
    cache[cachekey] = result
    return result