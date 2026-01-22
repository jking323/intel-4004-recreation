# Project Roadmap: RISC-4 (Pipelined Von Neumann)

**Target:** FPGA (CrossLink-NX-40) & Custom Silicon
**Architecture:** 5-Stage Pipeline (IF, ID, EX, MEM, WB) with Shared Bus Arbitration

---

## R1 - ISA & Pipeline Strategy (Phase 1)
**Goal:** Define an ISA that tolerates the Von Neumann bottleneck.
*Objective: Instruction set finalized and "Stall Strategy" defined.*

- [x] **ISA Definition**
    - [x] Define fixed-width instructions (likely 8-bit or 12-bit) to simplify the Fetch stage.
    - [x] Define Load/Store architecture (Memory access *only* via LD/ST instructions).
- [x] **Arbitration Logic Design**
    - [x] Define priority rules: Data Access (MEM stage) > Instruction Fetch (IF stage).
    - [x] Document the "Bubble Injection" strategy (inserting NOPs when IF is stalled).

**[ISA Reference Here!](https://github.com/jking323/risc-4)**

## R2 - Pipelined Datapath (Phases 2-3)
**Goal:** Build the 5-stage pipeline structure.
*Objective: Data flows from Fetch to Writeback correctly in isolation.*

- [ ] **Pipeline Registers**
    - [ ] Implement IF/ID, ID/EX, EX/MEM, MEM/WB registers.
- [ ] **Stage 1: Instruction Fetch (IF)**
    - [ ] Implement PC and "Next PC" logic.
    - [ ] Add `Stall` input signal to freeze PC during memory contention.
- [ ] **Stage 2: Decode (ID)**
    - [ ] Register File Read (2 ports).
    - [ ] Control Unit: Generate signals for ALU, MemRead, MemWrite.
- [ ] **Stage 3: Execute (EX)**
    - [ ] 4-bit ALU (Add, Sub, Logic).
    - [ ] Address Calculation (Base + Offset) for Load/Store.
- [ ] **Stage 4: Memory (MEM)**
    - [ ] **Crucial:** This stage outputs the Address/Data to the Bus Arbiter.
- [ ] **Stage 5: Writeback (WB)**
    - [ ] Select result (ALU Result vs Memory Data) to write back to RegFile.

## R3 - Hazard & Bus Arbitration Unit (Phases 4-5)
**Goal:** Solve the conflict between IF and MEM stages.
*Objective: Processor stalls Fetch automatically when doing Data IO.*

- [ ] **Bus Arbiter**
    - [ ] Input: Request from IF (Fetch) and Request from MEM (Load/Store).
    - [ ] Logic: If `MEM_Request == 1`, grant bus to MEM, assert `Stall_IF`.
    - [ ] Logic: If `MEM_Request == 0`, grant bus to IF.
- [ ] **Data Hazard Unit**
    - [ ] Implement Forwarding (Bypassing): Feed ALU result from EX/MEM or MEM/WB back to ID/EX inputs.
    - [ ] Implement Load-Use Hazard detection (Stall if dependent instruction follows Load).
- [ ] **Control Hazard Unit**
    - [ ] Implement Branch Flush: Clear IF/ID register if branch is taken.

## R4 - Unified Memory System (Phase 6)
**Goal:** Interface the pipeline to the single memory block.
*Objective: Single Port RAM serves both Code and Data requests.*

- [ ] **Memory Wrapper**
    - [ ] Instantiate Single-Port Block RAM.
    - [ ] Multiplex address input based on Arbiter Grant (PC vs ALU_Result).
- [ ] **IO Mapping**
    - [ ] Implement Memory Mapped I/O for GPIO/UART at high addresses.
- [ ] **Verification**
    - [ ] Write a test program with heavy Load/Store usage to verify the pipeline stalls correctly without corrupting the instruction stream.

## R5 - Synthesis & Performance (Phase 7)
**Goal:** Optimization.
*Objective: Functional GDS/Bitstream.*

- [ ] **Stall Analysis**
    - [ ] Measure CPI (Cycles Per Instruction). Due to Von Neumann, CPI will be > 1.0 for code with many Loads/Stores.
- [ ] **FPGA Implementation**
    - [ ] Map to CrossLink-NX-40.
    - [ ] Verify max frequency (Critical path is likely the Bus Mux -> Memory -> Data Setup).

## R6 - Software (Phase 8)
**Goal:** Code execution.

- [ ] **Assembler**
    - [ ] Update assembler to handle potential NOP padding if hardware hazard handling is simplified.
- [ ] **Demo**
    - [ ] "Pipeline Stress Test": A program that alternates Store and Arithmetic instructions rapidly.
