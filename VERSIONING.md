# Versioning Philosophy & Workflow

This project adheres to [Semantic Versioning 2.0.0](https://semver.org/).

Because this repository contains both software (tools/sim) and hardware (RTL/GDS), we map the version numbers as follows:

## 1. Version Format: `MAJOR.MINOR.PATCH`

### 💥 MAJOR (`X.0.0`) - Breaking / Milestone
Increments when we reach a physical or architectural inflection point.
* **Silicon Tapeout:** Any submission to a shuttle (e.g., SkyWater MPW).
* **ISA Break:** Changing the RISC-4 instruction encoding such that previous binaries fail.
* **Interface Break:** Changing the top-level pinout of the Faithful 4004 (breaking drop-in compatibility).

### ✨ MINOR (`0.X.0`) - Feat / Functionality
Increments when substantial functionality is added in a backwards-compatible manner.
* **Milestone Completion:** Finishing a major block (e.g., "M1 Serial Primitives Verified").
* **New Core:** Initial commit of a new experimental core.
* **Tooling:** Major upgrade to the simulation environment (e.g., switching simulators).

### 🐛 PATCH (`0.0.X`) - Fix / Chore
Increments for backwards-compatible bug fixes and maintenance.
* **RTL Fix:** Logic corrections that do not alter the spec (e.g., fixing a race condition).
* **Verification:** Fixing a bug in the testbench.
* **Refactor:** Folder restructuring or code cleanup.
* **Note:** Pure documentation changes (Journal, Typos) do **not** require a version bump.

---

## 2. Operational Workflow

We distinguish between **"Work in Progress"** (tracking via Git Hash) and **"Releases"** (tracking via SemVer).

### Daily Grind (The "Laptop Might Explode" Mode)
* **Goal:** Save work frequently.
* **Action:** Commit and push as often as needed.
* **Version:** **DO NOT** edit `VERSION.txt`.
* **Tracking:** The Makefile automatically appends the Git Hash (e.g., `0.0.1-a1b2c3d`) to build logs.

### Patch Workflow (Fixing a Bug)
* **Goal:** Mark a specific commit as a stable fix.
* **When:** You fixed a logic error or timing violation.
* **Steps:**
    1.  Edit `VERSION.txt` (Increment Patch: `0.0.1` -> `0.0.2`).
    2.  Commit: `git commit -m "fix(alu): correct carry propagation"`
    3.  **Tag (CLI):** `git tag v0.0.2`
    4.  Push: `git push && git push --tags`
* **Result:** A lightweight tag in Git history. No full GitHub Release required.

### Milestone Workflow (Completing a Goal)
* **Goal:** Celebrate a Roadmap Milestone (e.g., M1, M2).
* **When:** A major block is verified and ready for demo.
* **Steps:**
    1.  Edit `VERSION.txt` (Increment Minor: `0.0.2` -> `0.1.0`).
    2.  Update `docs/timeline/milestones.md` (Check the box).
    3.  Commit: `git commit -m "feat: complete M1 milestone"`
    4.  Push: `git push`
    5.  **Release (GUI):** Go to GitHub -> Releases -> Draft New Release.
        * Tag: `v0.1.0`
        * Title: "M1 - Serial Primitives Complete"
        * Description: Generate notes or paste from Design Journal.

---

## 3. Current Status
* **Current Version:** `0.0.1`
* **Phase:** Pre-Silicon Research & Infrastructure Setup.
