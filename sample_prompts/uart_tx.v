
module uart_tx(input clk, input rst, output reg done);
    always @(posedge clk or posedge rst) begin
        if (rst)
            done <= 0;
        else
            done <= 1;
    end
endmodule
