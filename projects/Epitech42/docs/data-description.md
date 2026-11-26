# Data description

Snapshot used in this version: `data/raw/2026-11-17/`, collected on 17 November 2026 at 09:15 UTC with `python src/collect.py`.

## Sources

We use two public Steam endpoints. Neither one needs an account or an API key.

| What | Endpoint | Notes |
| --- | --- | --- |
| Reviews by month | `https://store.steampowered.com/appreviewhistogram/<appid>` | Positive and negative review counts for every month since release. Steam does not document this endpoint. |
| Game announcements | `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/` | At most 100 posts per call. We page back with `enddate` until no new post comes back. We only ask for the `steam_community_announcements` feed, which is what the developers post themselves. |

The dashboard calls a third one, the store search (`https://store.steampowered.com/api/storesearch/`), only when someone looks up a game outside our five.

## What we keep

For each game the snapshot holds one JSON file named after the Steam app id:

- `reviews`: one row per month with the month start (Unix time, UTC), the number of positive reviews and the number of negative reviews.
- `announcements`: one row per post with its Steam id, date (Unix time), title and link.

We drop everything else the endpoints send back, including the post text and the author name. We collect nothing about players.

## Coverage

| Game | App id | Review months | Complete months | Reviews | Positive | First announcement | Posts | Posts after removing duplicates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Terraria | 105600 | May 2011 to Nov 2026 | 186 | 1,351,975 | 97.2% | Feb 2014 | 147 | 134 |
| Cyberpunk 2077 | 1091500 | Dec 2020 to Nov 2026 | 71 | 971,526 | 84.4% | Jun 2019 | 121 | 121 |
| No Man's Sky | 275850 | Aug 2016 to Nov 2026 | 123 | 335,391 | 80.5% | Aug 2016 | 155 | 131 |
| Stardew Valley | 413150 | Feb 2016 to Nov 2026 | 129 | 957,967 | 98.1% | Jan 2016 | 74 | 59 |
| Helldivers 2 | 553850 | Feb 2024 to Nov 2026 | 33 | 920,252 | 61.2% | Sep 2023 | 171 | 171 |

These totals are a little higher (5 to 81 more reviews per game) than the ones we wrote down a few hours earlier that day. Reviews kept coming in.

## Known gaps

- We have no review text. The page that serves it (`appreviews/<appid>?json=1`) redirected to the Steam home page for every game we tried, so we only work with counts.
- Counts are monthly. A patch released on the 28th shows up in a month where most reviews came before it.
- The month of collection isn't over yet, so the analysis leaves it out.
- Announcements do not cover the whole life of every game. Terraria's posts start in February 2014, three years after its first reviews, and there are none between April 2017 and April 2019. Stardew Valley has only two posts after December 2024.
- Steam returns some posts twice, with different ids but the same title on the same day. We keep one of each.
- The histogram gave the same total for Stardew Valley with the language set to English, to all, or left out. We think it counts reviews in every language, but Steam does not say so.
- None of the five histograms skipped a month.
- Deadlock is not in the list. Its review histogram comes back empty, even though Steam has 49 announcements for it.
