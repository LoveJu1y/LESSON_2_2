module top (now,inp,sysclock, ledo,clk,reset);
//input clk,reset;
//output [3:0] ano;
//output [6:0] leds;
//reg [3:0] cnt=4'b0000;
//wire [6:0] leds;

//assign ano=4'b0001;
//always @(posedge reset or posedge clk)
//begin
//    if(reset) cnt=4'b0000;
//    else begin
//        if(cnt==4'b1001) cnt<=4'b0000;
//        else cnt=cnt+1;
//     end
// end
//BCD7 bcd27seg (cnt,leds);


input sysclock,clk,reset,inp;
output ledo;
reg ledo;
output [2:0] now;
reg [2:0] now;
//output [6:0]led;
//reg [6:0]led;
wire clko;
debounce sss(.clk(sysclock),.key_i(clk),.key_o(clko));
//always @(posedge reset or posedge clko)
//begin 
//ledo=0;
//    if(reset) led=7'b0000000;
//    else begin
//     if(led[6]==1&&led[5]==1&&led[4]==0&&led[3]==1&&led[2]==0&&led[1]==1)
//       ledo=1;
//    led=led>>1;
//    led[6]=inp;

//    end
//    end
 always @(posedge reset or posedge clko)
    begin
    ledo=0;
   
    if(reset) now=3'b001;
    else begin
       case (now)
       3'b001:if(inp==1)now=3'b010;
       3'b010:if(inp==0)now=3'b011;
       3'b011:if(inp==1)now=3'b100;else now=3'b001;
       3'b100:if(inp==0)now=3'b101;else now=3'b010;
       3'b101:if(inp==1)now=3'b110;else now=3'b001;
       3'b110:if(inp==1)begin now=3'b010 ledo=1 end;else now=3'b101; 
    endcase
    end
    end
        

endmodule