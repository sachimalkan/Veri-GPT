
module tb_fifo_8x8;
    reg clk = 0;
    reg rst;
    wire done;

    fifo_8x8 uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing fifo_8x8");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
