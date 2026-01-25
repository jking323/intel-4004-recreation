"""
RISC-4 Register File Testbench
==============================
Location: root/sim/cocotb/test_regfile.py
RTL:      root/rtl/risc-4/regfile.sv
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import NextTimeStep, ReadOnly, RisingEdge, Timer

# ============================================================
# Helper Functions
# ============================================================


async def reset_dut(dut, duration_ns=20):
    """Apply asynchronous reset to DUT"""
    dut.rst_n.value = 0
    dut.write_enable.value = 0
    dut.write_addr.value = 0
    dut.write_data.value = 0
    dut.read_addr_a.value = 0
    dut.read_addr_b.value = 0

    await Timer(duration_ns, unit="ns")  # FIXED: unit not units
    dut.rst_n.value = 1
    await Timer(1, unit="ns")


async def write_register(dut, addr, data):
    """Write to a register (takes 1 clock cycle)"""
    dut.write_enable.value = 1
    dut.write_addr.value = addr
    dut.write_data.value = data
    await RisingEdge(dut.clk)
    dut.write_enable.value = 0


async def read_register(dut, port, addr):
    """Read from a register (combinational)

    IMPORTANT: This function exits ReadOnly phase before returning
    to allow subsequent writes.
    """
    if port == "a":
        dut.read_addr_a.value = addr
    else:
        dut.read_addr_b.value = addr

    await ReadOnly()  # Wait for combinational logic to settle

    # Capture the value while in ReadOnly
    if port == "a":
        value = dut.read_data_a.value
    else:
        value = dut.read_data_b.value

    # CRITICAL: Exit ReadOnly phase before returning
    await NextTimeStep()

    return value


# ============================================================
# TESTS
# ============================================================


@cocotb.test()
async def test_r0_always_zero(dut):
    """r0 must always read as zero (ISA requirement)"""
    clock = Clock(dut.clk, 10, unit="ns")  # FIXED: unit not units
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    # Test reading r0 after reset
    value = await read_register(dut, "a", 0)
    assert value == 0, f"r0 must read 0 after reset, got {value}"

    # Try to write to r0
    dut.write_enable.value = 1
    dut.write_addr.value = 0
    dut.write_data.value = 0xF
    await RisingEdge(dut.clk)
    dut.write_enable.value = 0

    # r0 should still be zero
    value = await read_register(dut, "a", 0)
    assert value == 0, f"r0 must ignore writes, got {value}"

    dut._log.info("✓ r0 hardwired to zero")


@cocotb.test()
async def test_basic_write_read(dut):
    """Test basic write and read operations"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    test_values = [(1, 0x3), (5, 0xA), (15, 0xF)]

    for addr, data in test_values:
        await write_register(dut, addr, data)
        value = await read_register(dut, "a", addr)
        assert value == data, f"r{addr}: expected 0x{data:X}, got 0x{value:X}"
        dut._log.info(f"✓ r{addr} = 0x{data:X}")


@cocotb.test()
async def test_dual_port_read(dut):
    """Test simultaneous reads from both ports"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    await write_register(dut, 3, 0x7)
    await write_register(dut, 8, 0xE)

    # Read from both ports simultaneously
    dut.read_addr_a.value = 3
    dut.read_addr_b.value = 8
    await ReadOnly()

    assert dut.read_data_a.value == 0x7, "Port A failed"
    assert dut.read_data_b.value == 0xE, "Port B failed"

    # Exit ReadOnly before finishing test
    await NextTimeStep()

    dut._log.info("✓ Dual-port read working")


@cocotb.test()
async def test_write_read_hazard(dut):
    """Test write-to-read timing in same cycle"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    # Pre-load r5 with 0x3
    await write_register(dut, 5, 0x3)

    # Setup simultaneous write and read
    dut.write_enable.value = 1
    dut.write_addr.value = 5
    dut.write_data.value = 0xA
    dut.read_addr_a.value = 5

    await ReadOnly()
    old_value = dut.read_data_a.value
    dut._log.info(f"Before clock: read_data_a = 0x{old_value:X} (expect 0x3)")

    await NextTimeStep()  # Exit ReadOnly
    await RisingEdge(dut.clk)

    await ReadOnly()
    new_value = dut.read_data_a.value
    dut._log.info(f"After clock: read_data_a = 0x{new_value:X} (expect 0xA)")

    await NextTimeStep()  # Exit ReadOnly

    assert old_value == 0x3, "Should see old value before clock"
    assert new_value == 0xA, "Should see new value after clock"
    dut._log.info("✓ Write-to-read hazard timing correct")


@cocotb.test()
async def test_reset_state(dut):
    """Verify reset behavior"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    dut._log.info("Register state after reset:")
    for i in range(16):
        value = await read_register(dut, "a", i)
        dut._log.info(f"  r{i:2d} = 0x{value:X}")
        assert value == 0, f"r{i} should reset to 0, got 0x{value:X}"

    dut._log.info("✓ All registers reset to 0")


@cocotb.test()
async def test_all_registers(dut):
    """Write and read all 16 registers"""
    clock = Clock(dut.clk, 10, unit="ns")
    cocotb.start_soon(clock.start())
    await reset_dut(dut)

    # Write unique pattern
    for i in range(16):
        await write_register(dut, i, i)

    # Verify
    for i in range(16):
        value = await read_register(dut, "a", i)
        if i == 0:
            assert value == 0, "r0 must stay 0"
        else:
            assert value == i, f"r{i}: expected {i}, got {value}"

    dut._log.info("✓ All registers functional")
