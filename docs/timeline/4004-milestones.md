# Project Roadmap: MCS-4 System Recreation

**Target:** FPGA (CrossLink-NX-40) & Silicon (GDSII)

---

## M1 - Serial Primitives Proven (Phases 1-2)
**Goal:** Verify fundamental serial architecture and clocking methodology.
*Objective: All shift registers and the serial ALU slice work in simulation. Clock generation verified.*

- [ ] **Clock Generation Logic**
    - [ ] Design non-overlapping 2-phase clock generator (phi_1, phi_2) from master clock.
    - [ ] Verify duty cycle and non-overlap periods in simulation.
    - [ ] Implement sync signal generation (sy).
- [ ] **Shift Register Primitives**
    - [ ] Design dynamic shift register cell (1-bit).
    - [ ] Cascade cells to create 4-bit and 12-bit shift registers.
    - [ ] Simulate data retention and propagation delay against phi_1/phi_2 timing.
- [ ] **Serial ALU Slice**
    - [ ] Implement bit-serial full adder.
    - [ ] Implement carry flip-flop and decimal adjust logic.
    - [ ] **Verification:** Create testbench to verify serial addition of two 4-bit numbers.

## M2 - Datapath Functional (Phases 3-5)
**Goal:** Complete the 4-bit internal architecture execution units.
*Objective: Register file, ALU, PC, and stack operate correctly in isolation. Can execute ALU operations and subroutine calls at unit level.*

- [ ] **Index Register File**
    - [ ] Implement 16 x 4-bit dynamic RAM array (or register equivalent).
    - [ ] Implement refresh logic (if using dynamic latches) or read/write control.
- [ ] **Address Stack & Program Counter**
    - [ ] Design 12-bit effective address register.
    - [ ] Design 3 x 12-bit return address stack (LIFO).
    - [ ] Implement stack pointer control logic.
    - [ ] Verify "push" and "pop" operations in simulation.
- [ ] **ALU Integration**
    - [ ] Connect Accumulator (ACC) and Carry (CY) to the serial adder.
    - [ ] Implement ALU control signals (Add, Sub, Logic, Rotate).
- [ ] **Datapath Verification**
    - [ ] **Unit Test:** Execute register-to-accumulator transfer.
    - [ ] **Unit Test:** Execute basic arithmetic (ADD, SUB) within the datapath.

## M3 - Instruction Execution (Phases 6-8)
**Goal:** Implement the "Brain" of the CPU to drive the Datapath.
*Objective: Control unit drives datapath. Can execute arbitrary instruction sequences with hardcoded instruction stream. All 46 instructions verified.*

- [ ] **Instruction Decoder (ID)**
    - [ ] Design OPR (Operation Register) and OPA (Operation Address) latches.
    - [ ] Implement Instruction Decoder PLA/Logic to map opcodes to control lines.
- [ ] **Timing & Control**
    - [ ] Implement Machine Cycle State Machine (A1, A2, A3, M1, M2, X1, X2, X3).
    - [ ] Define control signal assertions per machine state.
- [ ] **Instruction Verification**
    - [ ] Create `inst_testbench` with a hardcoded ROM model (internal).
    - [ ] **Group A:** Verify Machine Instructions (NOP, JCN, FIM, SRC, etc.).
    - [ ] **Group B:** Verify Input/Output & RAM Instructions (WRM, RDM, ADM).
    - [ ] **Group C:** Verify Accumulator Instructions (CLB, CLC, IAC, CMC, etc.).

## M4 - Standalone 4004 (Phase 9)
**Goal:** Externalize the bus to communicate with the outside world.
*Objective: External bus interface complete. 4004 can fetch from external memory model and execute programs.*

- [ ] **Bus Interface Unit**
    - [ ] Implement 4-bit bi-directional data bus (`D0-D3`).
    - [ ] Implement multiplexing logic for Address vs. Data/Instruction.
    - [ ] Implement CM-ROM and CM-RAM control line generation.
- [ ] **Bus Timing Verification**
    - [ ] Verify address transmission during states A1-A3.
    - [ ] Verify instruction fetch during M1-M2.
    - [ ] Verify data execution during X1-X3.
- [ ] **Integration Test**
    - [ ] Connect 4004 core to a behavioral Verilog memory model.
    - [ ] Execute a fetch-decode-execute loop from "external" memory.

## M5 - Memory Chips (Phases 10-12)
**Goal:** Recreate the support chips for the MCS-4 chipset.
*Objective: 4001, 4002, 4003 all functional individually.*

- [ ] **4001 ROM Design**
    - [ ] Design 256 x 8-bit mask programmable ROM array.
    - [ ] Implement address demultiplexing and chip select (CL) logic.
    - [ ] Implement 4-bit programmable I/O port.
- [ ] **4002 RAM Design**
    - [ ] Design 4 x 20 x 4-bit RAM array (Main memory + Status characters).
    - [ ] Implement RAM address decoding (Chip, Register, Character).
    - [ ] Implement 4-bit Output Port logic.
- [ ] **4003 Shift Register Design**
    - [ ] Design 10-bit serial-in, parallel-out shift register.
    - [ ] Implement enable and clock logic compatible with 4004.

## M6 - Full MCS-4 System Simulation (Phase 13)
**Goal:** System-level verification of the complete chipset.
*Objective: Complete system with all 16 ROM, 16 RAM, shift registers. Test program executes correctly.*

- [ ] **Top-Level Integration**
    - [ ] Instantiate 4004 CPU.
    - [ ] Instantiate memory banks (up to 16x 4001, 16x 4002).
    - [ ] Interconnect via 4-bit global bus and control lines.
- [ ] **System Verification**
    - [ ] **Load Test Program:** Busicom calculator firmware or similar complex logic.
    - [ ] **Simulation:** Run full-system RTL simulation.
    - [ ] **Debug:** Trace instruction flow and I/O port activity.

## M7 - FPGA Running (Phase 14)
**Goal:** Move from simulation to hardware emulation.
*Objective: Hardware execution on CrossLink-NX-40. Can observe internal state, execute test programs.*

- [ ] **Synthesis & Constraints**
    - [ ] Map asynchronous logic/latches to FPGA primitives (if necessary for stability).
    - [ ] Define Pin Constraints File (PCF) for CrossLink-NX-40 dev board.
    - [ ] Set timing constraints for target clock frequency.
- [ ] **Instrumentation**
    - [ ] Integrate Logic Analyzer (Reveal / ChipScope equivalent) to monitor internal bus.
    - [ ] Map I/O ports to LEDs/Buttons for physical verification.
- [ ] **Hardware Bring-up**
    - [ ] Flash bitstream.
    - [ ] Verify reset sequence and clock stability.
    - [ ] Run "Blinky" program via 4004 instructions.

## M8 - Silicon Ready (Phase 15)
**Goal:** Physical design for manufacturing.
*Objective: GDS complete, DRC/LVS clean, ready for tapeout queue.*

- [ ] **Physical Design (RTL-to-GDS)**
    - [ ] **Synthesis:** Run logical synthesis with target PDK standard cell library.
    - [ ] **Floorplanning:** Define core area, pin placement, and power rings.
    - [ ] **Placement:** Place standard cells and macros.
    - [ ] **CTS:** Clock Tree Synthesis (crucial for multiphase clocks).
    - [ ] **Routing:** Global and detailed routing.
- [ ] **Sign-off**
    - [ ] **STA:** Static Timing Analysis (Setup/Hold violations).
    - [ ] **DRC:** Design Rule Check (Geometric violations).
    - [ ] **LVS:** Layout vs. Schematic (Connectivity verification).
- [ ] **Final Deliverable**
    - [ ] Stream out GDSII file.
