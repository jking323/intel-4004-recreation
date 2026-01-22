# Project Roadmap: Pipelined 4004 (High-Performance Core)

**Target:** FPGA (CrossLink-NX-40) / Optimization Study

---

## P1 - Parallel Primitives (Phases 1-2)
**Goal:** Replace bit-serial logic with parallel 4-bit logic to support single-cycle execution stages.
*Objective: 4-bit Parallel ALU and Register File operational.*

- [ ] **Parallel ALU Design**
    - [ ] Implement 4-bit parallel adder (Ripple Carry or Lookahead).
    - [ ] Implement single-cycle Decimal Adjust (DAA) logic.
    - [ ] Verify 4-bit logic operations (AND, OR, XOR, Rotate) complete in <1 clock cycle.
- [ ] **Multi-Port Register File**
    - [ ] Design 16x4-bit Register File with 2 Read Ports / 1 Write Port.
    - [ ] **Verification:** Test simultaneous read/write operations to verify setup/hold times.

## P2 - Pipeline Infrastructure (Phases 3-4)
**Goal:** Establish the skeletal structure of the pipeline.
*Objective: IF, ID, EX, MEM, WB registers defined and connected.*

- [ ] **Pipeline Registers**
    - [ ] Implement IF/ID, ID/EX, EX/MEM, MEM/WB pipeline registers.
    - [ ] Define control signal propagation through stages.
- [ ] **Instruction Fetch (IF) Stage**
    - [ ] Design Program Counter (PC) with increments logic.
    - [ ] Implement Instruction Memory Interface (Harvard architecture separation required internally).

## P3 - Hazard Control (Phases 5-7)
**Goal:** Solve the inherent dangers of pipelining (Data and Control Hazards).
*Objective: Processor runs sequences of dependent instructions without data corruption.*

- [ ] **Data Hazard Unit**
    - [ ] Implement Forwarding Unit (bypass results from MEM or WB stage back to EX).
    - [ ] Implement Stall Unit (detect Load-Use hazards).
- [ ] **Control Hazard Unit**
    - [ ] Implement "Flush" logic for pipeline registers.
    - [ ] Implement Branch Comparator in ID stage (to resolve branches early).
    - [ ] **Verification:** Run "torture test" with back-to-back dependencies and branches.

## P4 - Bus Adaptation (Phase 8)
**Goal:** Interface the fast internal pipeline with the slow, multiplexed 4004 external bus.
*Objective: Prefetch buffer hides external bus latency.*

- [ ] **Bus Controller**
    - [ ] Implement state machine to translate internal requests to standard 4004 bus cycles (A1-X3).
- [ ] **Instruction Prefetch Buffer**
    - [ ] Design a FIFO (4-8 instructions deep) to decouple Fetch stage from external bus.
    - [ ] Implement logic to pause pipeline if FIFO is empty (starvation).

## P5 - Full Execution Verification (Phase 9)
**Goal:** Ensure the pipelined core behaves exactly like a standard 4004.
*Objective: Runs Busicom calculator ROMs correctly, but faster.*

- [ ] **Compatibility Testing**
    - [ ] Run standard 4004 test suite.
    - [ ] Verify specific 4004 quirks (e.g., DAA behavior, page boundary crossings).
- [ ] **Performance Benchmarking**
    - [ ] Compare cycle count of Pipelined vs. Serial core for standard tasks.
