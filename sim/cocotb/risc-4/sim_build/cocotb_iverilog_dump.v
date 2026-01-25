module cocotb_iverilog_dump();
initial begin
    $dumpfile("sim_build/regfile.fst");
    $dumpvars(0, regfile);
end
endmodule
