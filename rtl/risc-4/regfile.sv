module regfile (
    input  logic        clk,
    input  logic        rst_n,
    input  logic        write_enable,
    input  logic [3:0]  write_addr,
    input  logic [3:0]  write_data,
    input  logic [3:0]  read_addr_a,
    output logic [3:0]  read_data_a,
    input  logic [3:0]  read_addr_b,
    output logic [3:0]  read_data_b
);

    // Storage: 16 registers × 4 bits
    logic [3:0] registers [15:0];

    // ============================================================
    // WRITE LOGIC
    // ============================================================
    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            // Question 2: Do you need to reset all registers?
            // Hint: What does your ISA spec say about power-on state?
            // For now, let's leave them undefined (X) except r0
            integer i;
            for (i = 0; i < 16; i++) begin
                registers[i] <= 4'h0;
            end

        end else begin
            // Question 3: How do you prevent writes to r0?
            // Write your condition here:

            if (write_enable && write_addr != 4'd0) begin
                registers[write_addr] <= write_data;
            end
        end
    end

    // ============================================================
    // READ LOGIC (Asynchronous - Combinational)
    // ============================================================

    // Question 4: Should r0 be special-cased before or after the array lookup?
    // Think about synthesis: What's cheaper?

    // Port A
    assign read_data_a = (read_addr_a == 4'd0) ? 4'h0 : registers[read_addr_a];

    // Port B
    assign read_data_b = (read_addr_b == 4'd0) ? 4'h0 : registers[read_addr_b];

endmodule
