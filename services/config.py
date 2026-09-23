#### DAQ CONFIG ####
## This is the documented sensor calibrations, as well as the port configurations in use on the DAQ Box.
## To use the LabJack Source, duplicate this file and name it `config.py`, uncomment and modify as needed.
## NOTE: If `config.py` is updated, please also update this file as required
## Last modified 2026-09-22 - Jason Xu for pump pathfinder spin test 1

from calibration import Connection, LinearCalibration, Sensor, ThermistorCalibration

# pyright: basic

# LabJack Stream Configuration
# Configured at 25 readings per read, and 1000 readings per second per channel.
SCANS_PER_READ = 1
SCAN_RATE = 10000


def setup():
    """
    Setup the sensors.
    """

    Sensor("[NPT-201] Pneumatics", "AIN87", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[NPT-301] Nitrogen Pressurization", "AIN95", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-302] Fuel Tank", "AIN86", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-401] Pump Inlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-402] Pump Outlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-403] Coolant Inlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-404] Coolant Outlet", "AIN94", 10, Connection.SINGLE,
        LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
