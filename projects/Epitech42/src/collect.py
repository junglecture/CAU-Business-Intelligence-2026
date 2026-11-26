import json
import sys
from datetime import date
from pathlib import Path

from steam import fetch_game

ROOT = Path(__file__).resolve().parent.parent


def main():
    """Saves the games of config/games.json in data/raw/<today>/, one JSON file per game.

    Prints one line per game. Stops if today's folder already exists.
    """
    games = json.loads((ROOT / "config" / "games.json").read_text())
    folder = ROOT / "data" / "raw" / date.today().isoformat()
    if folder.exists():
        sys.exit(f"{folder.relative_to(ROOT)} already exists. Snapshots are never overwritten.")
    folder.mkdir(parents=True)
    for game in games:
        data = fetch_game(game["appid"], game["name"])
        if not data["reviews"]:
            print(f"{game['name']}: no review data, skipped")
            continue
        (folder / f"{game['appid']}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
        total = sum(r["positive"] + r["negative"] for r in data["reviews"])
        print(f"{game['name']}: {len(data['reviews'])} months, {total:,} reviews, {len(data['announcements'])} announcements")


if __name__ == "__main__":
    main()
