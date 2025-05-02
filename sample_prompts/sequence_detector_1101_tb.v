
module tb_sequence_detector_1101;
    reg clk = 0;
    reg rst;
    wire done;

    sequence_detector_1101 uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing sequence_detector_1101");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
