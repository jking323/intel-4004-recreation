module alu (
    input  logic [3:0] operand_a,
    input  logic [3:0] operand_b,
    input  logic [3:0] alu_op,
    input  logic       carry_in,
    output logic [3:0] result,
    output logic       carry_out,
    output logic       zero
);

    localparam logic [3:0] ALU_ADD = 4'b0000;
    localparam logic [3:0] ALU_ADC = 4'b0001;
    localparam logic [3:0] ALU_SUB = 4'b0010;
    localparam logic [3:0] ALU_SBB = 4'b0011;
    localparam logic [3:0] ALU_AND = 4'b0100;
    localparam logic [3:0] ALU_OR  = 4'b0101;
    localparam logic [3:0] ALU_XOR = 4'b0110;
    localparam logic [3:0] ALU_SLT = 4'b0111;

    //==========================================================================
    // Internal Signals (ALL DECLARED HERE)
    //==========================================================================
    logic [4:0] add_result;
    logic [4:0] sub_result;
    logic       sub_borrow;

    logic [4:0] extended_a;  // Shared for add/sub
    logic [4:0] extended_b;  // Shared for add/sub

    logic [3:0] and_result;
    logic [3:0] or_result;
    logic [3:0] xor_result;

    logic [3:0] slt_result;
    logic       is_less_than;
    logic       sign_a;
    logic       sign_b;

    //==========================================================================
    // Arithmetic Operations
    //==========================================================================
    always_comb begin
        extended_a = {1'b0, operand_a};
        extended_b = {1'b0, operand_b};

        if (carry_in == 1'b0)
            add_result = extended_a + extended_b;
        else
            add_result = extended_a + extended_b + carry_in;
    end

    always_comb begin
        extended_a = {1'b0, operand_a};
        extended_b = {1'b0, operand_b};

        if (carry_in == 1'b0)
            sub_result = extended_a - extended_b;
        else
            sub_result = extended_a - extended_b - 5'b00001;
        sub_borrow = sub_result[4];
    end

    //==========================================================================
    // Logical Operations
    //==========================================================================
    assign and_result = operand_a & operand_b;
    assign or_result  = operand_a | operand_b;
    assign xor_result = operand_a ^ operand_b;

    //==========================================================================
    // Comparison Operation (Signed)
    //==========================================================================
    always_comb begin
        sign_a = operand_a[3];
        sign_b = operand_b[3];

        if (sign_a != sign_b) begin
            is_less_than = sign_a;
        end else begin
            is_less_than = (operand_a < operand_b);
        end

        slt_result = {3'b000, is_less_than};
    end

    //==========================================================================
    // Result Multiplexer
    //==========================================================================
    always_comb begin
        case (alu_op)
            ALU_ADD: result = add_result[3:0];
            ALU_ADC: result = add_result[3:0];
            ALU_SUB: result = sub_result[3:0];
            ALU_SBB: result = sub_result[3:0];
            ALU_AND: result = and_result;
            ALU_OR:  result = or_result;
            ALU_XOR: result = xor_result;
            ALU_SLT: result = slt_result;
            default: result = 4'b0000;
        endcase
    end

    //==========================================================================
    // Carry/Borrow Output Generation
    //==========================================================================
    always_comb begin
        case (alu_op)
            ALU_ADD: carry_out = add_result[4];
            ALU_ADC: carry_out = add_result[4];
            ALU_SUB: carry_out = sub_result[4];
            ALU_SBB: carry_out = sub_result[4];
            ALU_AND: carry_out = 1'b0;
            ALU_OR:  carry_out = 1'b0;
            ALU_XOR: carry_out = 1'b0;
            ALU_SLT: carry_out = 1'b0;
            default: carry_out = 1'b0;
        endcase
    end

    //==========================================================================
    // Zero Flag Generation
    //==========================================================================
    assign zero = (result == 4'b0000);

endmodule
