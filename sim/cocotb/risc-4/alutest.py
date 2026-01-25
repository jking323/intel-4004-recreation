#!/usr/bin/env python3
"""
RISC-4 ALU Testbench (cocotb)
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer

# ALU Operation Encodings
ALU_ADD = 0x0
ALU_ADC = 0x1
ALU_SUB = 0x2
ALU_SBB = 0x3
ALU_AND = 0x4
ALU_OR = 0x5
ALU_XOR = 0x6
ALU_SLT = 0x7


@cocotb.test()
async def test_add_basic(dut):
    """Test basic ADD operations"""

    # Test 1: 5 + 3 = 8
    dut.operand_a.value = 0x5
    dut.operand_b.value = 0x3
    dut.alu_op.value = ALU_ADD
    dut.carry_in.value = 0
    await Timer(1, unit="ns")  # Let combinational logic settle

    assert dut.result.value == 0x8, f"ADD 5+3: Expected 0x8, got 0x{dut.result.value:x}"
    assert dut.carry_out.value == 0, (
        f"ADD 5+3: Expected carry=0, got {dut.carry_out.value}"
    )
    assert dut.zero.value == 0, f"ADD 5+3: Expected zero=0, got {dut.zero.value}"

    # Test 2: F + 1 = 0 (with carry and zero)
    dut.operand_a.value = 0xF
    dut.operand_b.value = 0x1
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0, f"ADD F+1: Expected 0x0, got 0x{dut.result.value:x}"
    assert dut.carry_out.value == 1, (
        f"ADD F+1: Expected carry=1, got {dut.carry_out.value}"
    )
    assert dut.zero.value == 1, f"ADD F+1: Expected zero=1, got {dut.zero.value}"

    # Test 3: 0 + 0 = 0 (zero without carry)
    dut.operand_a.value = 0x0
    dut.operand_b.value = 0x0
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0
    assert dut.carry_out.value == 0
    assert dut.zero.value == 1


@cocotb.test()
async def test_sub_basic(dut):
    """Test basic SUB operations"""

    dut.alu_op.value = ALU_SUB
    dut.carry_in.value = 0

    # Test 1: 5 - 3 = 2
    dut.operand_a.value = 0x5
    dut.operand_b.value = 0x3
    await Timer(1, unit="ns")

    assert dut.result.value == 0x2
    assert dut.carry_out.value == 0  # No borrow
    assert dut.zero.value == 0

    # Test 2: 3 - 5 = E (with borrow, from ISA spec example)
    dut.operand_a.value = 0x3
    dut.operand_b.value = 0x5
    await Timer(1, unit="ns")

    assert dut.result.value == 0xE, f"SUB 3-5: Expected 0xE, got 0x{dut.result.value:x}"
    assert dut.carry_out.value == 1, (
        f"SUB 3-5: Expected carry=1 (borrow), got {dut.carry_out.value}"
    )

    # Test 3: 5 - 5 = 0 (zero result)
    dut.operand_a.value = 0x5
    dut.operand_b.value = 0x5
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0
    assert dut.carry_out.value == 0
    assert dut.zero.value == 1


@cocotb.test()
async def test_logical_ops(dut):
    """Test AND, OR, XOR operations"""

    dut.carry_in.value = 0

    # Test AND
    dut.alu_op.value = ALU_AND
    dut.operand_a.value = 0b1010
    dut.operand_b.value = 0b1100
    await Timer(1, unit="ns")

    assert dut.result.value == 0b1000
    assert dut.carry_out.value == 0  # Logical ops clear carry
    assert dut.zero.value == 0

    # Test OR
    dut.alu_op.value = ALU_OR
    dut.operand_a.value = 0b1010
    dut.operand_b.value = 0b0101
    await Timer(1, unit="ns")

    assert dut.result.value == 0b1111
    assert dut.carry_out.value == 0

    # Test XOR
    dut.alu_op.value = ALU_XOR
    dut.operand_a.value = 0b1010
    dut.operand_b.value = 0b1010
    await Timer(1, unit="ns")

    assert dut.result.value == 0b0000
    assert dut.zero.value == 1  # XOR with self = 0


@cocotb.test()
async def test_slt_signed_comparison(dut):
    """Test SLT (Set Less Than) - Signed comparison"""

    dut.alu_op.value = ALU_SLT
    dut.carry_in.value = 0

    # Test 1: Both positive, 3 < 7 → TRUE
    dut.operand_a.value = 0x3  # +3
    dut.operand_b.value = 0x7  # +7
    await Timer(1, unit="ns")

    assert dut.result.value == 0x1, (
        f"SLT +3 < +7: Expected 0x1 (true), got 0x{dut.result.value:x}"
    )
    assert dut.carry_out.value == 0  # SLT clears carry
    assert dut.zero.value == 0

    # Test 2: Both positive, 7 < 3 → FALSE
    dut.operand_a.value = 0x7  # +7
    dut.operand_b.value = 0x3  # +3
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0, (
        f"SLT +7 < +3: Expected 0x0 (false), got 0x{dut.result.value:x}"
    )

    # Test 3: Negative < Positive → TRUE
    dut.operand_a.value = 0xF  # -1 in two's complement
    dut.operand_b.value = 0x7  # +7
    await Timer(1, unit="ns")

    assert dut.result.value == 0x1, (
        f"SLT -1 < +7: Expected 0x1 (true), got 0x{dut.result.value:x}"
    )

    # Test 4: Positive < Negative → FALSE
    dut.operand_a.value = 0x7  # +7
    dut.operand_b.value = 0xF  # -1
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0, (
        f"SLT +7 < -1: Expected 0x0 (false), got 0x{dut.result.value:x}"
    )

    # Test 5: Both negative, -8 < -1 → TRUE
    dut.operand_a.value = 0x8  # -8
    dut.operand_b.value = 0xF  # -1
    await Timer(1, unit="ns")

    assert dut.result.value == 0x1, (
        f"SLT -8 < -1: Expected 0x1 (true), got 0x{dut.result.value:x}"
    )

    # Test 6: Both negative, -1 < -8 → FALSE
    dut.operand_a.value = 0xF  # -1
    dut.operand_b.value = 0x8  # -8
    await Timer(1, unit="ns")

    assert dut.result.value == 0x0, (
        f"SLT -1 < -8: Expected 0x0 (false), got 0x{dut.result.value:x}"
    )


# TODO: Add these tests
@cocotb.test()
async def test_adc_with_carry(dut):
    """Test ADC (Add with Carry)"""
    # TODO: Implement ADC tests
    dut.alu_op.value = ALU_ADC
    dut.operand_a.value = 0x5
    dut.operand_b.value = 0x2
    dut.carry_in.value = 1  # ← Previous carry
    await Timer(1, unit="ns")

    assert dut.result.value == 0x8  # 5 + 2 + 1 = 8
    pass


@cocotb.test()
async def test_sbb_with_borrow(dut):
    """Test SBB (Subtract with Borrow)"""
    # TODO: Implement SBB tests
    dut.alu_op.value = ALU_SBB
    dut.operand_a.value = 0x5
    dut.operand_b.value = 0x2
    dut.carry_in.value = 1  # ← Previous borrow
    await Timer(1, unit="ns")

    assert dut.result.value == 0x2  # 5 - 2 - 1 = 2
    pass
