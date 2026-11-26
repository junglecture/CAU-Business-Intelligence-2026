# Epitech42

Business Intelligence — Fall 2026 · Chung-Ang University

**Steam update impact dashboard**

## Project overview

For five Steam games, how do the number of reviews and the share of positive reviews change after a major update, compared with each game's usual trend?

A producer or community manager at a game studio could use the answer when choosing what to ship next: a big content update or smaller patches. The dashboard shows how players reacted to past updates of five games. It can't tell a studio which update to make next.

### Data

We use public Steam pages, with no account and no personal data. For each game we collect the monthly count of positive and negative reviews, and the date and title of every announcement. We could not get the text of the reviews.

| Game | Months of data | Reviews | Positive |
| --- | --- | --- | --- |
| Stardew Valley | 130 | 957,924 | 98.1% |
| Terraria | 187 | 1,351,950 | 97.2% |
| Cyberpunk 2077 | 72 | 971,445 | 84.4% |
| No Man's Sky | 124 | 335,386 | 80.5% |
| Helldivers 2 | 34 | 920,205 | 61.2% |

We checked these figures on 17 November 2026. We left Deadlock out because Steam shows no review data for it.

### Method

1. Date each update from its announcement.
2. Label it as a major update, a patch or other, using its title.
3. Compare the months before and after each major update.
4. Compare with a baseline: the game's review trend without an update.

We check a sample of labels by hand and report the error rate.

### Limits

- The numbers are monthly, so we see big updates but not small patches.
- A change after an update does not prove the update caused it. Sales, seasons and review bombing also move reviews.
- Only players who write reviews are counted.

## Team

| Member | Role | Main tasks |
| --- | --- | --- |
| Yanis Senovic | Project leader | question, BI decision, Python environment, data description, label check, error analysis, demo video, submission |
| Luc Simon | Developer | data collection and cleaning, labels, baseline, dashboard, slides file |
| Aloys Mangin | Documentation | ETL diagram, final report, AI use disclosure, contributions record |

## Plan and tasks

| Week | Target date | Goal |
| --- | --- | --- |
| 1 | 23 Nov | pick the games, test and save the data, write the data description |
| 2 | 30 Nov | clean the data, label the updates, build the baseline and the before/after comparison |
| 3 | 7 Dec | build the dashboard, check errors, prepare the slides for the week 15 presentation |
| 4 | 14 Dec | demo video, final report, README, submission |

We track the work as 26 issues in our team repository. Each one has a single owner:

### Yanis

- Week 1: confirm the five games; write the research question and the BI decision on one page; set up the Python environment and the folders; write the data description; ask the professor about the demo format
- Week 2: check a sample of labels by hand and measure the error rate
- Week 3: write the error analysis and the limits; review the slides and rehearse the 7-minute talk (with Aloys)
- Week 4: record the demo video; submit the final package

### Luc

- Week 1: write the collection script; save a dated snapshot of the raw data
- Week 2: clean the data into one monthly table per game; label each update; build the baseline; compute the before/after comparison
- Week 3: build the interactive dashboard; create the presentation file; bonus: search any game by name
- Week 4: write the run instructions and test a clean install; check the code from a fresh clone

### Aloys

- Week 2: draw the data model and ETL diagram
- Week 3: review the slides and rehearse (with Yanis)
- Week 4: write the final report, the AI use disclosure and the contributions record; collect the supporting files

## Code and reproducibility

The analysis code will land here before the final deadline. For now this folder has the Python environment and the empty project folders.

We use Python 3.14. Run this inside `projects/Epitech42`:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, run `.venv\Scripts\activate` instead of the `source` line. `requirements.txt` pins the versions we tested with, and git ignores the `.venv` folder.

| Folder | What goes in it |
| --- | --- |
| `config/` | the list of games and the labelling rules |
| `src/` | collection, cleaning, labelling and comparison code |
| `data/raw/` | dated snapshots of the Steam data |
| `data/processed/` | monthly tables built from a snapshot |
| `dashboard/` | the Streamlit dashboard |
| `docs/` | data description, method, ETL diagram |
| `report/` | figures and the final report |

## Deliverables

- [x] Proposal: this README
- [ ] Source code and run instructions
- [ ] Presentation slides (week 15)
- [ ] Demo video
- [ ] Final report, with AI use disclosure and contributions record

## Data and licensing

We only use public Steam data, collected without an account. This folder holds no credentials and no personal information.
