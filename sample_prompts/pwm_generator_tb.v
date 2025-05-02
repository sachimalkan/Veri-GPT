
module tb_pwm_generator;
    reg clk = 0;
    reg rst;
    wire done;

    pwm_generator uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing pwm_generator");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
