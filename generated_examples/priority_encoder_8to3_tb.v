
module tb_priority_encoder_8to3;
    reg clk = 0;
    reg rst;
    wire done;

    priority_encoder_8to3 uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing priority_encoder_8to3");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
