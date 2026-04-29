# DevOps Job Application Automation

> AI-powered CLI pipeline that scrapes DevOps job listings, scores them against
> my CV using a LLaMA model, auto-tailors the CV, and compiles a ready-to-send PDF.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA-purple)
![LaTeX](https://img.shields.io/badge/CV-LaTeX%20%2B%20pdflatex-orange)
![SQLite](https://img.shields.io/badge/DB-SQLite-lightgrey)
![Status](https://img.shields.io/badge/status-active-brightgreen)

> ⚠️ **This repository is a public showcase.**
> The source code is maintained privately.
> Feel free to reach out if you'd like a demo or a walkthrough.

---

## 🎯 Problem

Applying to DevOps roles manually is time-consuming:
finding relevant jobs, reading each description, adapting the CV,
compiling the PDF — repeated 10–20 times a week.

This tool reduces that entire workflow to a single CLI command.

---

## ⚙️ How it works

```
$ python main.py --location ***** --min-score 70
```

```
[scraper]   Fetching jobs from Adzuna API...        32 jobs found
[dedup]     Checking SQLite store...                18 new jobs
[matcher]   Running LLaMA fit scoring...            7 jobs above threshold
[tailorer]  Rewriting CV for: "Senior DevOps @ Adyen"
[compiler]  Compiling LaTeX → PDF...               ✓ output/adyen_cv.pdf
...
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    CLI entry point                  │
└────────────────────────┬────────────────────────────┘
                         │
         ┌───────────────▼───────────────┐
         │           Scraper             │
         │  Adzuna API · ** filter       │
         │  relevance pre-scoring        │
         └───────────────┬───────────────┘
                         │
         ┌───────────────▼───────────────┐
         │         SQLite store          │
         │  deduplication across runs    │
         └───────────────┬───────────────┘
                         │
         ┌───────────────▼───────────────┐
         │           Matcher             │
         │  Groq LLaMA · semantic match  │
         │  CV ↔ job description scoring │
         └───────────────┬───────────────┘
                         │  (score ≥ threshold)
         ┌───────────────▼───────────────┐
         │           Tailorer            │
         │  keyword injection            │
         │  section rewriting per job    │
         └───────────────┬───────────────┘
                         │
         ┌───────────────▼───────────────┐
         │           Compiler            │
         │  LaTeX template → pdflatex    │
         │  → per-job PDF output         │
         └───────────────────────────────┘
```

---

## 🧰 Tech stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Job data | Adzuna Jobs API |
| LLM | Groq API — LLaMA 3 70B |
| CV format | LaTeX + pdflatex |
| Storage | SQLite (deduplication) |
| CLI | argparse |
| Output | Per-job tailored PDF |

---

## 📐 Design principles

- **Strict separation of concerns** — each module (scraper / matcher / tailorer / compiler) is independent and unit-testable
- **Deduplication by default** — SQLite store prevents reprocessing already-seen job IDs across runs
- **Threshold filtering** — only jobs above a configurable fit score trigger the tailoring pipeline
- **Stateless compilation** — the LaTeX compiler receives a self-contained payload; no global state

---

## 📊 Results

| Metric | Before | After |
|---|---|---|
| Time per application | ~25 min | ~4 min |
| Manual CV edits | Every job | Zero |
| Jobs reviewed / hour | ~3 | ~18 |
| **Time saved** | — | **~80%** |

---

## 🗂️ Project structure (overview)

```
devops-job-automation/
├── main.py               # CLI entry point
├── scraper/              # Adzuna API client + filtering
├── matcher/              # LLM scoring logic
├── tailorer/             # CV section rewriting
├── compiler/             # LaTeX → PDF pipeline
├── store/                # SQLite deduplication
├── templates/            # LaTeX CV base template
├── output/               # Generated PDFs (gitignored)
└── config.yaml           # Thresholds, API settings
```

> Source code is private. This overview reflects the actual module structure.

---

## 🚀 Usage (summary)

```bash
# Run full pipeline for set Location, min fit score 70
python main.py --location ***** --min-score 70

# Dry run (fetch + score only, no CV generation)
python main.py --dry-run

# Target specific job title
python main.py --title "platform engineer" --location *****
```

---

## 👤 Author

**Marouani Nesrine** — Cloud DevOps Engineer
📍 Tunis 
🔗 [LinkedIn](https://www.linkedin.com/in/nesrine-marouani-547651143/)

---

*Built to automate my own job search. Currently targeting
DevOps / Platform Engineering roles .*
