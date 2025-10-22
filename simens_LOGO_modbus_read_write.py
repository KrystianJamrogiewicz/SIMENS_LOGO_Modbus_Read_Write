from pyModbusTCP.client import ModbusClient
from time import sleep

c = ModbusClient(host="192.168.0.3", auto_open=True, auto_close=True, port=502)
c.write_single_coil(8266, 0)        # Write Q1 by M11
c.write_single_coil(8267, 0)        # Write Q2 by M12
c.write_single_coil(8268, 0)        # Write Q3 by M13
c.write_single_coil(8269, 1)        # Write Q4 by M14

while True:

    M3_I3_D = c.read_coils(8258, 1)     # Read digital I3 by M3
    M4_I4_D = c.read_coils(8259, 1)     # Read digital I4 by M4
    M5_I5_D = c.read_coils(8260, 1)     # Read digital I5 by M5
    M6_I6_D = c.read_coils(8261, 1)     # Read digital I6 by M6

  #  I1_AI3 = c.read_input_registers(2, 1)

    AM1_AI3_I1 = c.read_holding_registers(528, 1)        # Read I1 Analog by AM1
    AM2_AI4_I2 = c.read_holding_registers(529, 1)        # Read I2 Analog by AM2
    AM7_AI1_I7 = c.read_holding_registers(534, 1)        # Read I7 Analog by AM7
    AM8_AI2_I8 = c.read_holding_registers(535, 1)        # Read I8 Analog by AM8

    print(" M3", M3_I3_D, " M4", M4_I4_D, " M5", M5_I5_D, " M6", M6_I6_D, " AM1:", AM1_AI3_I1, " AM2:", AM2_AI4_I2, " AM7:", AM7_AI1_I7, " AM8:", AM8_AI2_I8)

    sleep(1)
