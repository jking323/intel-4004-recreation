# ============================================================
# RISC-4 Cocotb Testbench Makefile
# ============================================================

# Global Defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
WAVES = 1

# Default test to run if not specified (e.g. "make")
TEST ?= alutest

# Logic to switch between ALU and REGFILE
ifeq ($(TEST),alu)
    # --- ALU Configuration ---
    VERILOG_SOURCES = $(PWD)/../../../rtl/risc-4/alu.sv
    TOPLEVEL = alu
    MODULE = alutest
else
    # --- Regfile Configuration (Default) ---
    VERILOG_SOURCES = $(PWD)/../../../rtl/risc-4/regfile.sv
    TOPLEVEL = regfile
    MODULE = regtest
endif

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
