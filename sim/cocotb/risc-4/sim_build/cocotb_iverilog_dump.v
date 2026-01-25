module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/alu.fst");
    $dumpvars(0, alu);
end
endmodule
