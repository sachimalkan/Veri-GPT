
module tb_uart_rx;
    reg clk = 0;
    reg rst;
    wire done;

    uart_rx uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing uart_rx");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
