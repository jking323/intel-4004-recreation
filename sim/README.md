# Simulation & Verification

This folder contains all the testbenches and simulation infrastructure for the RISC-4 processor project. I'm using cocotb for Python-based testing because writing Verilog testbenches makes me want to throw my laptop out the window.

## Directory Structure
```
sim/
├── cocotb/              # Python testbenches (cocotb framework)
│   ├── Makefile         # Simulation runner (uses Icarus Verilog)
│   ├── test_regfile.py  # Register file tests
│   └── sim_build/       # Auto-generated build artifacts (gitignored)
│
├── verilog_tb/          # Traditional Verilog testbenches (if I hate myself)
│   └── (empty for now)
│
└── waveforms/
    ├── saved_views/     # GTKWave .gtkw config files
    │   └── regfile_phase1.gtkw
    └── screenshots/     # Waveform screenshots for documentation
        └── regfile_phase1_overview.png
```

## Quick Start

### Running Tests
```bash
cd sim/cocotb
make                # Run all tests
make waves          # Run tests + open GTKWave
make clean          # Clean up build artifacts
```

### Viewing Waveforms

After running tests, the waveform data lives in `sim_build/regfile.fst`.

**Load with saved view:**
```bash
gtkwave sim_build/regfile.fst ../waveforms/saved_views/regfile_phase1.gtkw
```

**Or start fresh:**
```bash
gtkwave sim_build/regfile.fst
```

## Test Status

### Phase 1: Register File ✅
- **Module:** `rtl/risc-4/regfile.sv`
- **Tests:** `cocotb/test_regfile.py`
- **Status:** 6/6 tests passing
- **Verified:**
  - r0 hardwired to zero (ISA requirement)
  - Dual-port reads work simultaneously
  - Write-to-read hazard timing correct
  - All 16 registers accessible

### Phase 2: ALU 🚧
*Coming next...*

## Waveform Management

### Saved Views (.gtkw files)
These are GTKWave configuration files that remember:
- Which signals are visible
- Signal order and grouping
- Zoom level and time markers
- Color highlighting

**Why save these?** Because setting up the same waveform view 50 times during debug makes you question your life choices.

### Screenshots
Exported images for documentation, blog posts, or showing off to people who don't care about 4-bit processors.

**When to screenshot:**
- Found an interesting bug (before and after fix)
- Demonstrating a specific timing behavior
- Proof that something actually works

## Tools Used

- **Simulator:** Icarus Verilog (iverilog/vvp)
- **Test Framework:** cocotb (Python-based)
- **Waveform Viewer:** GTKWave
- **Build System:** GNU Make

### Installation (macOS)
```bash
brew install icarus-verilog gtkwave
pip3 install cocotb
```

## Writing Tests

cocotb tests are just Python functions with the `@cocotb.test()` decorator:
```python
@cocotb.test()
async def test_something(dut):
    """Test description"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)
    
    # Your test logic here
    dut.input_signal.value = 0x5
    await RisingEdge(dut.clk)
    assert dut.output_signal.value == 0xA
```

**Why cocotb over Verilog?**
- Actual programming language (Python > Verilog for testbenches)
- Easy assertions and logging
- Can use NumPy, random, etc.
- Waveforms still work exactly the same

## Known Issues

### Cocotb API Changes
Newer cocotb versions changed `units=` to `unit=` (singular). All tests updated to use `unit="ns"`.

### ReadOnly Phase Violations
If you see `RuntimeError: Attempting settings a value during the ReadOnly phase`, you forgot to call `await NextTimeStep()` after `await ReadOnly()`. This bit me like 4 times while writing the register file tests.

### GTKWave Zoom
If your waveform looks like solid noise, you're zoomed out too far. Click and drag on the time axis to zoom into a specific range. Or press Ctrl+G and jump to a specific time.

## Debug Tips

1. **Start with the test output** - cocotb logs everything
2. **Add print statements** - `dut._log.info(f"Signal = {value:X}")`
3. **Use markers in GTKWave** - Right-click time axis → Drop Named Marker
4. **Focus on clock edges** - Almost everything happens on rising edge
5. **Check one test at a time** - Don't try to debug 6 failing tests at once

## What's Next

- [ ] ALU implementation and tests
- [ ] Instruction decoder
- [ ] Pipeline stages (IF, ID, EX, MEM, WB)
- [ ] Hazard detection and forwarding
- [ ] Full CPU integration test

The register file was easy. The pipeline control is where things get spicy.

---

*Last updated: January 2026*  
*If you're reading this and confused, check the main README in the repo root.*
