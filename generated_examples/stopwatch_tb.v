
module tb_stopwatch;
    reg clk = 0;
    reg rst;
    wire done;

    stopwatch uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing stopwatch");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
