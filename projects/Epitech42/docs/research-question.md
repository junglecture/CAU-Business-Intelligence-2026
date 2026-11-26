# Research question and BI decision

## The question

For five Steam games, how do the number of reviews and the share of positive reviews change around major updates, compared with each game's usual trend?

## Who uses the answer

A producer or community manager at a game studio, when the team has to choose what to ship next: one big content update or a run of smaller patches.

## What they decide

We don't pick the next update for them. The dashboard shows how players reacted to past updates of five well known games. With it, the person deciding can see what usually happens to review volume and to the share of positive reviews after a big update, and after a month of patches.

## What we compare against

Looking at the month after an update tells you little by itself. Review counts move with sales, the seasons and the age of the game. So for every update we fit a straight line through the six months before it (on a log scale for the review count), extend it over the update month and the two months after, and measure how far the real numbers land from it. We call that line the game's usual trend.

To judge whether a gap is big, we compute the same gap for every month of the game that had no major update. A change counts as unusual when it is at least twice the standard deviation of those ordinary months.

## What would count as an answer

- Volume and positive share both above the trend after major updates, and more often than after patch months: big updates look worth it for how players react.
- Only volume above the trend: big updates bring players back, but they don't change what players think of the game.
- Nothing moves: the choice has to rest on something else, like cost or the roadmap.

## What it does not answer

It can't prove that an update caused a change. We don't see sales, player counts or revenue either. And the five games are our pick, all of them hits, so the results may not hold for smaller games.
