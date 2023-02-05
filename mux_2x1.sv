
`timescale 1ns/1ps
module mux_2x1(
    input  logic i0,
    input  logic i1,
    input  logic s,
    output logic o
);
    assign o = ((~s) & i0) + (s & i1);

initial begin
    $dumpfile("dump.vcd");
    $dumpvars;
end
endmodule