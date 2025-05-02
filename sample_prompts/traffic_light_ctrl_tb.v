
module tb_traffic_light_ctrl;
    reg clk = 0;
    reg rst;
    wire done;

    traffic_light_ctrl uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing traffic_light_ctrl");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
