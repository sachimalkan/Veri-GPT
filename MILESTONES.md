#  VeriGPT-HDL Project Milestones

This document outlines the planned and completed milestones for the VeriGPT-HDL research and development effort.

---

##  Q1 2025 – Foundational Setup
- [x] Defined research scope and motivation for LLM-guided HDL generation
- [x] Created initial GitHub repository and codebase structure
- [x] Implemented basic prompt ingestion and GPT-4 HDL synthesis
- [x] Integrated Icarus Verilog for testbench-driven simulation

---

##  Q2 2025 – Simulation & Feedback Loop
- [x] Implemented simulation-based verification using testbenches
- [x] Developed basic feedback loop for multi-round HDL correction
- [ ] Add structured error categorization (syntax, logic, instability)
- [ ] Support parameterized testbench generation

---

##  Q3 2025 – Self-Refinement and Prompt Intelligence
- [ ] Chain-of-Thought prompting for FSM/state logic reliability
- [ ] Include output waveform trace analysis
- [ ] Auto-refine prompt using simulation failure logs
- [ ] Support multiple architectural templates (pipeline, hierarchy)

---

##  Q4 2025 – Formal Methods and Evaluation
- [ ] Integrate Yosys/Symbiyosys for formal equivalence checking
- [ ] Add metrics.py to evaluate latency, area, power heuristics
- [ ] Compare against hand-written HDL in accuracy and efficiency
- [ ] Write academic paper and benchmark results

---

## Publications & Presentation Goals
- Draft whitepaper: July 2025
- Academic submission (DATE, ICCAD): October 2025
- Project showcase/demo on GitHub Pages: Q4 2025

---

Feel free to track updates via issues and commits.

> "VeriGPT-HDL: Towards Trustworthy LLM-Driven Chip Design Workflows"
