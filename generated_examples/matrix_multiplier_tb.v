
module tb_matrix_multiplier;
    reg clk = 0;
    reg rst;
    wire done;

    matrix_multiplier uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing matrix_multiplier");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
