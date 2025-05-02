
module tb_alu_4bit;
    reg clk = 0;
    reg rst;
    wire done;

    alu_4bit uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing alu_4bit");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
