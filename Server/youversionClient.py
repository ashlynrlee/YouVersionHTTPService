import requests

from Server.errors import UpstreamError

urlBase = "https://api.youversion.com"
appKey = "1gqBksQ6ec6GdOCCDfMrmyV6x5UlZGDWSkLxmCTWjGgrg5hm"
auth = "x-yvp-app-key" 

def getData(url:str):
    try: 
        response = requests.get(url, headers={auth: appKey},timeout=5)
    except Exception as e:
        raise UpstreamError(f"API request failed: {e}")

    if response.status_code != 200:
        raise UpstreamError(f"API returned {response.status_code}")

    data = response.json()
    return data

def getPassageIdForDay(day: int) -> str:
    url = f"{urlBase}/v1/verse_of_the_days/{day}"

    data = getData(url)
    if "passage_id" not in data:
        raise UpstreamError("API response missing passage_id")

    return data["passage_id"] 

def getPassageText(version_id: int, passage_id: str) -> dict:
    url= f"{urlBase}/v1/bibles/{version_id}/passages/{passage_id}?format=text"
    data = getData(url)

    if "reference" not in data or "content" not in data:
        raise UpstreamError("Passage API response missing fields")

    return { "reference": data["reference"], "content": data["content"]}
