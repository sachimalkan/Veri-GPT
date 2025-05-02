
module tb_debounce_circuit;
    reg clk = 0;
    reg rst;
    wire done;

    debounce_circuit uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing debounce_circuit");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
