
module tb_gray_code_counter;
    reg clk = 0;
    reg rst;
    wire done;

    gray_code_counter uut(.clk(clk), .rst(rst), .done(done));

    always #5 clk = ~clk;

    initial begin
        $display("Testing gray_code_counter");
        rst = 1; #10;
        rst = 0; #20;
        if (done) $display("PASS"); else $display("FAIL");
        $finish;
    end
endmodule
