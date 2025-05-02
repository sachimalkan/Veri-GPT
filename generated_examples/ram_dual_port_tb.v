
module tb_ram_dual_port;
    reg clk = 0;
    reg rst;
    wire done;

    ram_dual_port uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing ram_dual_port");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
