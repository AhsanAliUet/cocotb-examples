# test_mux_2x1.py

import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_simple(dut):
    """ Simple 2 to 1 mux"""

    # clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    # cocotb.start_soon(clock.start())  # Start the clock

    for i in range(10):
        print("Running test number", i)
        i0 = random.randint(0, 1)
        i1 = random.randint(0, 1)
        s  = random.randint(0, 1)
        dut.i0.value = i0
        dut.i1.value = i1
        dut.s.value  = s
        await Timer(2, units="ns")
        if (s):
            assert dut.o.value == i1, "Randomised test failed with: i0 = {A}, i1 = {B}, o = {X}".format(
            A=dut.i0.value, B=dut.i1.value, X=dut.o.value)
        else:
            assert dut.o.value == i0, "Randomised test failed with: i0 = {A}, i1 = {B}, s = {C}, o = {X}".format(
            A=dut.i0.value, B=dut.i1.value, C = dut.s.value, X=dut.o.value)