---
name: 🐛 Bug Report
about: Create a report to help us improve the silicon
title: "[BUG] Brief description of the error"
labels: ["bug"]
assignees: ''
---

### 📍 Location
*Which core is affected?*
- [ ] Faithful 4004
- [ ] Pipelined 4004
- [ ] RISC-4

### 📝 Description
*What happened? (e.g., "The Accumulator did not clear after a CLB instruction")*

### 🔁 Reproduction Steps
1. Run test `make test_alu`
2. Observer signal `acc_out` at timestamp 450ns
3. See error

### 📉 Expected vs. Actual Behavior
*Expected: Accumulator = 0000*
*Actual: Accumulator = 1010*
