
#set_property -dict {PACKAGE_PIN R2 IOSTANDARD LVCMOS33} [get_ports {bcd[3]}]
#set_property -dict {PACKAGE_PIN M4 IOSTANDARD LVCMOS33} [get_ports {bcd[2]}]
#set_property -dict {PACKAGE_PIN N4 IOSTANDARD LVCMOS33} [get_ports {bcd[1]}]
#set_property -dict {PACKAGE_PIN R1 IOSTANDARD LVCMOS33} [get_ports {bcd[0]}]

#set_property -dict {PACKAGE_PIN B4 IOSTANDARD LVCMOS33} [get_ports {leds[0]}]
#set_property -dict {PACKAGE_PIN A4 IOSTANDARD LVCMOS33} [get_ports {leds[1]}]
#set_property -dict {PACKAGE_PIN A3 IOSTANDARD LVCMOS33} [get_ports {leds[2]}]
#set_property -dict {PACKAGE_PIN B1 IOSTANDARD LVCMOS33} [get_ports {leds[3]}]
#set_property -dict {PACKAGE_PIN A1 IOSTANDARD LVCMOS33} [get_ports {leds[4]}]
#set_property -dict {PACKAGE_PIN B3 IOSTANDARD LVCMOS33} [get_ports {leds[5]}]
#set_property -dict {PACKAGE_PIN B2 IOSTANDARD LVCMOS33} [get_ports {leds[6]}]

#set_property -dict {PACKAGE_PIN G2 IOSTANDARD LVCMOS33} [get_ports {ano[0]}]
#set_property -dict {PACKAGE_PIN C2 IOSTANDARD LVCMOS33} [get_ports {ano[1]}]
#set_property -dict {PACKAGE_PIN C1 IOSTANDARD LVCMOS33} [get_ports {ano[2]}]
#set_property -dict {PACKAGE_PIN H1 IOSTANDARD LVCMOS33} [get_ports {ano[3]}]

set_property -dict {PACKAGE_PIN R15 IOSTANDARD LVCMOS33} [get_ports clk]
set_property -dict {PACKAGE_PIN U4 IOSTANDARD LVCMOS33} [get_ports reset]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {clk}]

set_property -dict {PACKAGE_PIN N4 IOSTANDARD LVCMOS33} [get_ports inp]

#set_property -dict {PACKAGE_PIN J2 IOSTANDARD LVCMOS33} [get_ports {led[0]}]
#set_property -dict {PACKAGE_PIN J3 IOSTANDARD LVCMOS33} [get_ports {led[1]}]
#set_property -dict {PACKAGE_PIN H4 IOSTANDARD LVCMOS33} [get_ports {led[2]}]
#set_property -dict {PACKAGE_PIN J4 IOSTANDARD LVCMOS33} [get_ports {led[3]}]
#set_property -dict {PACKAGE_PIN G3 IOSTANDARD LVCMOS33} [get_ports {led[4]}]
#set_property -dict {PACKAGE_PIN G4 IOSTANDARD LVCMOS33} [get_ports {led[5]}]
#set_property -dict {PACKAGE_PIN F6 IOSTANDARD LVCMOS33} [get_ports {led[6]}]

set_property -dict {PACKAGE_PIN K2 IOSTANDARD LVCMOS33} [get_ports {ledo}]
set_property -dict {PACKAGE_PIN P17 IOSTANDARD LVCMOS33} [get_ports {sysclock}]
set_property -dict {PACKAGE_PIN G3 IOSTANDARD LVCMOS33} [get_ports {now[0]}]
set_property -dict {PACKAGE_PIN G4 IOSTANDARD LVCMOS33} [get_ports {now[1]}]
set_property -dict {PACKAGE_PIN F6 IOSTANDARD LVCMOS33} [get_ports {now[2]}]
