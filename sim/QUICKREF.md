# Simulation Quick Reference

## Common Commands
```bash
# Run tests
cd sim/cocotb && make

# View waveforms
gtkwave sim_build/regfile.fst

# Clean build
make clean

# Run specific test
TESTCASE=test_r0_always_zero make
```

## GTKWave Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl + G` | Go to time |
| `Ctrl + F` | Find next edge |
| `Ctrl + Mouse Wheel` | Zoom in/out |
| `Left-drag` | Zoom to selection |
| `Alt + Wheel` | Pan left/right |
| `Home` / `End` | Jump to start/end |

## Debugging Workflow

1. Test fails → Read cocotb output for which assertion
2. Find time of failure in log
3. Press `Ctrl+G` in GTKWave, jump to that time
4. Zoom in (click-drag 20ns before/after)
5. Check: What should happen vs. what actually happened
6. Fix RTL
7. `make clean && make`
8. Repeat until green ✅

## Test Organization

Each test file should have:
- Helper functions (reset_dut, write_register, etc.) at top
- Tests in order of complexity (simple → complex)
- Clear docstrings explaining what's being tested
- Informative log messages (`dut._log.info()`)

## When Things Break

**Test won't run:**
- Check Makefile paths (VERILOG_SOURCES)
- Verify cocotb installed: `cocotb-config --version`
- Check simulator: `iverilog -v`

**Waveform looks wrong:**
- You're zoomed out too far (99% of the time)
- Signal names don't match RTL (check hierarchy in SST panel)
- Forgot to enable waveform dump (should be automatic with cocotb)

**Simulation hangs:**
- Forgot to start the clock: `cocotb.start_soon(clock.start())`
- Waiting for signal that never changes
- Infinite loop in RTL (ctrl+C and check waveform)
