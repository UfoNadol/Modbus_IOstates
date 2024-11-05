from pyModbusTCP.client import ModbusClient
from time import sleep

u: ModbusClient = ModbusClient(host="192.168.0.3", auto_open=True, port=502, auto_close=True);

while True:
    analog = u.read_input_registers(0, 2)
    digital = u.read_discrete_inputs(0, 6)
    print('wartości analogowe :', analog)
    print('wartości cyfrowe :', digital)
    sleep(0.5)
