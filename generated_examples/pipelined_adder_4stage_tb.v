
module tb_pipelined_adder_4stage;
    reg clk = 0;
    reg rst;
    wire done;

    pipelined_adder_4stage uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing pipelined_adder_4stage");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
