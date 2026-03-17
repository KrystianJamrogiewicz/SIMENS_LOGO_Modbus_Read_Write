# Siemens LOGO! - Python Modbus TCP Communication

Data transfer between Siemens LOGO! and a PC using **Modbus TCP** and Python code. The script reads input states (digital/analog) and controls the PLC outputs.

---

## Hardware
* **PLC:** Siemens LOGO! 8 / 24CE (6ED1052-2CC08-0BA1)
* **PC:** Connected via Ethernet

---

## Software
* **LOGO! Soft Comfort:** For PLC configuration and programing.
* **Python IDE:** e.g., PyCharm.

---

## Code Logic & Libraries

The project uses the **pyModbusTCP** library to communicate with the PLC via port **502**.

### Main Functions:
* `ModbusClient`: Manages the connection (IP: `192.168.0.3`).
* `write_single_coil`: Controls digital outputs/markers (e.g., M11-M14).
* `read_coils`: Reads digital input states from markers (e.g., M3-M6).
* `read_holding_registers`: Reads analog values (e.g., AM1, AM7, AM8).

---

## Installation

Install the required library via pip:

```bash
pip install pyModbusTCP
