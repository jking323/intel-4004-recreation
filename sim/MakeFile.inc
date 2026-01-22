# Internal include for Cocotb execution
include $(shell cocotb-config --makefiles)/Makefile.sim

# Waveform Generation
ifeq ($(WAVES), 1)
	PLUSARGS += +dumpvars+build/$(SIM)/dump.vcd
endif
