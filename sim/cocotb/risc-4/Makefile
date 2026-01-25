# ============================================================
# RISC-4 Cocotb Testbench Makefile
# ============================================================

# Simulator selection (icarus = Icarus Verilog, free & fast)
SIM ?= icarus

# RTL source files (adjust path to your regfile.sv)
VERILOG_SOURCES = $(PWD)/../../../rtl/risc-4/regfile.sv

# Python testbench module (no .py extension)
MODULE = regtest

# Top-level HDL module name (must match module name in regfile.sv)
TOPLEVEL = regfile

# Language
TOPLEVEL_LANG = verilog

# Waveform generation
WAVES = 1

# Include cocotb's simulation rules
include $(shell cocotb-config --makefiles)/Makefile.sim

# ============================================================
# Convenience targets
# ============================================================

.PHONY: clean waves

# View waveforms (after running tests)
waves:
	@echo "Opening waveform viewer..."
	gtkwave regfile.vcd &

# Clean build artifacts
clean::
	rm -rf __pycache__
	rm -rf sim_build
	rm -f results.xml
	rm -f *.vcd
