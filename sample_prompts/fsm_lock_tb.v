
module tb_fsm_lock;
    reg clk = 0;
    reg rst;
    wire done;

    fsm_lock uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing fsm_lock");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
