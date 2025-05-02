
module tb_barrel_shifter_8bit;
    reg clk = 0;
    reg rst;
    wire done;

    barrel_shifter_8bit uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing barrel_shifter_8bit");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
