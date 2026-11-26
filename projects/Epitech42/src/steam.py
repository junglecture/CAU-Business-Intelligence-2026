import time

import requests

HISTOGRAM = "https://store.steampowered.com/appreviewhistogram/{}"
NEWS = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
SEARCH = "https://store.steampowered.com/api/storesearch/"


def get_json(url, params):
    """Calls a Steam URL and returns the JSON. Tries 3 times, waiting a bit longer each time.

    @param url: Steam URL (str)
    @param params: query parameters (dict)
    @return: the JSON answer (dict)
    @raise RuntimeError: if Steam never answers
    """
    for attempt in range(3):
        try:
            r = requests.get(url, params=params, timeout=30)
            if r.status_code == 200:
                return r.json()
        except requests.RequestException:
            pass
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Steam did not answer: {url}")


def fetch_reviews(appid):
    """Gets the positive and negative review counts per month from the review histogram.

    @param appid: Steam app id (int)
    @return: list of {date, positive, negative}, date in Unix time. Empty if the game has no data.
    """
    data = get_json(HISTOGRAM.format(appid), {"l": "english"})
    rollups = (data.get("results") or {}).get("rollups") or []
    return [
        {"date": r["date"], "positive": r["recommendations_up"], "negative": r["recommendations_down"]}
        for r in rollups
    ]


def fetch_announcements(appid):
    """Gets every developer announcement. Steam gives 100 per call, so we page back with enddate.

    @param appid: Steam app id (int)
    @return: list of {gid, date, title, url}, oldest first
    """
    items, seen, end = [], set(), None
    while True:
        params = {"appid": appid, "count": 100, "maxlength": 1, "feeds": "steam_community_announcements"}
        if end:
            params["enddate"] = end
        batch = get_json(NEWS, params).get("appnews", {}).get("newsitems", [])
        fresh = [i for i in batch if i["gid"] not in seen]
        if not fresh:
            break
        for i in fresh:
            seen.add(i["gid"])
            items.append({"gid": i["gid"], "date": i["date"], "title": i["title"].strip(), "url": i["url"]})
        if len(batch) < 100:
            break
        end = min(i["date"] for i in batch) - 1
    return sorted(items, key=lambda i: i["date"])


def search_games(term):
    """Searches the Steam store by name, for the dashboard's "Search another game" page. Soundtracks are left out.

    @param term: text typed by the user (str)
    @return: list of {appid, name}
    """
    data = get_json(SEARCH, {"term": term, "l": "english", "cc": "us"})
    items = data.get("items", [])
    return [{"appid": i["id"], "name": i["name"]} for i in items
            if i.get("type") == "app" and "soundtrack" not in i["name"].lower()]


def fetch_game(appid, name):
    """Collects reviews and announcements for one game.

    @param appid: Steam app id (int)
    @param name: game name (str)
    @return: dict with appid, name, collected_at, reviews, announcements
    """
    return {
        "appid": appid,
        "name": name,
        "collected_at": int(time.time()),
        "reviews": fetch_reviews(appid),
        "announcements": fetch_announcements(appid),
    }
