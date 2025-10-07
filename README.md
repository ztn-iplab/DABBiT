# DABBiT – Concept Drift Experiments (Keystroke & Mouse)

This repo contains Jupyter notebooks for the DABBiT framework. **Raw datasets are not stored here.**

## Datasets (official sources)
- KeystrokeMouse-TZ (our dataset): https://github.com/ztn-iplab/banking_CA
- CMU Keystroke: https://www.cs.cmu.edu/~keystroke/
- DFL Mouse: https://www.ms.sapientia.ro/~manyi/DFL.html

## Getting the data
Run:
    python scripts/fetch_data.py
This clones KeystrokeMouse-TZ into `data/raw/keystrokemouse_tz/` and prints manual steps for CMU & DFL.

## Layout
notebooks/  scripts/  data/ (ignored)  README.md  .gitignore  requirements.txt
