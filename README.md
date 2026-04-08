# Smart Email Assistant Environment

## Overview
This project simulates a real-world email triage and response system for AI agents.

## Tasks
1. Classification (Easy) — classify email type
2. Extraction (Medium) — extract date and priority
3. Response (Hard) — generate a professional reply

## Environment Design
- Multi-step interaction
- Agent must complete tasks sequentially
- State includes task and stage

## Action Space
- Structured actions with content

## Observation Space
- Email text
- Metadata (task, stage)

## Reward Design
- Classification: 0–1
- Extraction: partial scoring
- Response: keyword-based scoring
- Rewards provided at each step

## Baseline
Deterministic fallback ensures reproducible score of 1.0

## Run
```bash
pip install -r requirements.txt
python inference.py