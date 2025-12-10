Concept Drift Taxonomy for Behavioral Biometrics (One-Pager)

This one-pager summarizes the **Causal Drift Taxonomy** introduced in the DABBiT framework for continuous authentication using keystroke and mouse dynamics.  
The taxonomy provides a structured way to understand how and why user behavioral patterns evolve — either naturally or under adversarial influence — in real-world internet banking environments.

It is based on the accepted paper:

Festus Edward Ndalama, Patrick Mutabazi, Yuzo Taenaka, Youki Kadobayashi, "DABBiT: A Drift-Adaptive Behavioral Biometrics Framework for Continuous Authentication in Tanzanian Internet Banking", AAIML 2026.


 What is Concept Drift in Behavioral Biometrics?

Concept drift refers to changes in user behavior over time such that previously learned authentication models become less accurate.  
In behavioral biometrics (keystroke & mouse), drift arises from:

- Cognitive or emotional variations  
- Physical or environmental conditions  
- Device or system changes  
- Adversarial mimicry (e.g., malware automating human-like behavior)  

Understanding the source of drift is essential for building adaptive and secure authentication models.


The Drift Taxonomy (Four Major Categories)

1. Cognitive & Behavioral Drift
Changes caused by natural human variability:
- Fatigue or stress  
- Mood and emotional state  
- Cognitive load or distraction  
- Learning and habit evolution  
- Task complexity  

2. Identity & Input Drift
Changes in how input is produced:
- User switching / impersonation  
- Typing style change (language, layout)  
- Sitting position or device posture  
- Hardware differences (keyboard/mouse)  
- Touchpad vs. mouse transitions  

3. Environmental & System Drift
External conditions affecting behavior or capture:
- Software/OS updates  
- Network or system latency  
- Ambient conditions (lighting, noise)  
- Device performance fluctuations  
- Background processes and UI response time  

4. Security & Adversarial Drift
Intentional manipulation of biometric signals:
- Malware injecting timing delays   
- Replay or scripted behavior automation  
- Overlay-based UI manipulation  
- Man-in-the-middle distortion  
- Synthetic keystroke/mouse generation  


Temporal Drift Patterns

Drift can appear in different temporal forms:

- Sudden / abrupt – immediate shift (e.g., malware attack)  
- Gradual – behavior slowly changes over time  
- Incremental – continuous but small shifts  
- Recurring – patterns reappear (e.g., weekly usage rhythms)  

These forms guide how frequently adaptation should occur.


Taxonomy Diagram


[Concept Drift Taxonomy](taxonomy.png)



Why This Taxonomy Matters for DABBiT

The taxonomy enables:

- Identification of **root causes** of drift  
- Selection of appropriate **drift-detection methods** (ADWIN, DDM, embedding distance)  
- Designing **adaptive thresholds** that respond to natural or adversarial changes  
- Hardening behavioral models against **humanized automation attacks**  
- Supporting **federated learning**, where each bank branch experiences different drift patterns  

It forms the conceptual foundation for the Drift-Adaptive Behavioral Biometrics Framework (DABBiT)** and guides experimental evaluation.


 Maintainer

Festus Edward Ndalama 
PhD Researcher – Behavioral Biometrics & Cybersecurity  
Nara Institute of Science and Technology (NAIST), Japan  
GitHub: https://github.com/ztn-iplab/DABBiT
