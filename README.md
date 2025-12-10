# 🧬 DABBiT – Drift-Adaptive Behavioral Biometrics Framework  
### Continuous Authentication Under Concept Drift (Keystroke & Mouse Dynamics)

This repository contains Jupyter notebooks, scripts, and documentation supporting **DABBiT**, a drift-adaptive behavioral biometrics framework for continuous authentication in internet banking environments.

> 🔒 **Raw datasets are NOT stored in this repository** due to privacy restrictions.

---

## 📚 Background

DABBiT introduces:

- A **Causal Taxonomy of Concept Drift** for behavioral biometrics  
- A **drift-aware adaptive authentication pipeline**  
- An **adversarial simulation layer** (e.g., Herodotus-style humanized malware mimicry)  
- Multi-modal fusion: **keystroke + mouse + contextual signals**  
- Prototype extension toward **federated learning** for distributed banking systems  

The conceptual taxonomy was formalized in the paper:

**Festus Edward Ndalama, Patrick Mutabazi, Yuzo Taenaka, Youki Kadobayashi,  
“DABBiT: A Drift-Adaptive Behavioral Biometrics Framework for Continuous Authentication in Tanzanian Internet Banking,”  
AAIML 2026.**

---

## 📥 Datasets (Official Sources)

- **KeystrokeMouse-TZ (our dataset)**  
  https://github.com/ztn-iplab/banking_CA  

- **CMU Keystroke Dataset**  
  https://www.cs.cmu.edu/~keystroke/

- **DFL Mouse Dataset**  
  https://www.ms.sapientia.ro/~manyi/DFL.html  

---

## 📥 Getting the Data

Run:

```bash
python scripts/fetch_data.py
