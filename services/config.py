#### DAQ CONFIG ####
## This is the documented sensor calibrations, as well as the port configurations in use on the DAQ Box.
## To use the LabJack Source, duplicate this file and name it `config.py`, uncomment and modify as needed.
## NOTE: If `config.py` is updated, please also update this file as required
## Last modified 2026-09-13 - Jason Xu for pump spin test 1

from calibration import Connection, LinearCalibration, Sensor, ThermistorCalibration

# pyright: basic

# LabJack Stream Configuration
# Configured at 25 readings per read, and 1000 readings per second per channel.
SCANS_PER_READ = 25
SCAN_RATE = 1000


def setup():
    """
    Setup the sensors.
    """

    Sensor("[PT-202] Pneumatics", "AIN87", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[PT-310] Nitrogen Fill Upstream", "AIN95", 10, Connection.SINGLE,
        LinearCalibration(1/100*1000/0.016, -0.004*1000/0.016, "psi"))
    Sensor("[PT-302] Tank", "AIN86", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[PT-404] Pump Outlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[PT-407] Coolant Inlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[PT-507] Coolant Outlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
