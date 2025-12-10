Concept Drift Taxonomy for Behavioral Biometrics (One-Pager)

This one-pager summarizes the **Causal Drift Taxonomy** introduced in the DABBiT framework for continuous authentication using keystroke and mouse dynamics.  
The taxonomy provides a structured way to understand how and why user behavioral patterns evolve — either naturally or under adversarial influence — in real-world internet banking environments.

It is based on the accepted paper:

Festus Edward Ndalama, Patrick Mutabazi, Yuzo Taenaka, Youki Kadobayashi, "DABBiT: A Drift-Adaptive Behavioral Biometrics Framework for Continuous Authentication in Tanzanian Internet Banking", AAIML 2026.

Download the Full Taxonomy (High-Resolution PDF)

👉 [**Taxonomy of Concept Drift in Behavioral Biometrics (PDF)**](Taxonomy_of_Concept_Drift_in_Behavioral_Biometrics.pdf)

---

## 🔍 What is Concept Drift in Behavioral Biometrics?

Concept drift refers to changes in user behavior over time such that previously learned authentication models become less accurate.  
In behavioral biometrics (keystroke & mouse), drift arises from:

- Cognitive or emotional variations  
- Physical or environmental conditions  
- Device or system changes  
- Adversarial mimicry (e.g., malware automating human-like behavior)

Understanding the **source** of drift is essential for building adaptive and secure authentication models.

---

## 🧭 The Drift Taxonomy (Four Major Categories)

### **1. Cognitive & Behavioral Drift**  
Changes caused by natural human variability:
- Fatigue or stress  
- Mood and emotional state  
- Cognitive load or distraction  
- Learning and habit evolution  
- Task complexity  

### **2. Identity & Input Drift**  
Changes in how input is produced:
- User switching / impersonation  
- Typing style change (language, layout)  
- Sitting position or device posture  
- Hardware differences (keyboard/mouse)  
- Touchpad vs. mouse transitions  

### **3. Environmental & System Drift**  
External factors affecting behavior or data capture:
- Software/OS updates  
- Network or system latency  
- Ambient conditions (lighting, noise)  
- Device performance fluctuations  
- UI responsiveness & background processes  

### **4. Security & Adversarial Drift**  
Intentional manipulation of biometric signals:
- Malware injecting timing delays  
- Synthetic keystroke/mouse generation  
- Replay or scripted automation  
- Overlay-based UI manipulation  
- Man-in-the-middle distortion  

---

## ⏱️ Temporal Drift Patterns

Concept drift may appear in different temporal forms:

- **Sudden / Abrupt** – immediate shift (e.g., malware attack)  
- **Gradual** – behavior changes slowly over time  
- **Incremental** – continuous small shifts  
- **Recurring** – patterns reappear (e.g., weekly rhythms)

These forms guide how frequently adaptation should occur.

---

## 🖼️ Taxonomy Diagram


![Concept Drift Taxonomy](taxonomy.png)


 Maintainer

Festus Edward Ndalama 
PhD Researcher – Behavioral Biometrics & Cybersecurity  
Nara Institute of Science and Technology (NAIST), Japan  
GitHub: https://github.com/ztn-iplab/DABBiT
