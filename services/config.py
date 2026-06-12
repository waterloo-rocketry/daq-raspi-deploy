#### EXAMPLE CONFIG ####
## This is the documented sensor calibrations, as well as the port configurations in use on the DAQ Box.
## To use the LabJack Source, duplicate this file and name it `config.py`, uncomment and modify as needed.
## NOTE: If `config.py` is updated, please also update this file as required
## Last modified 2026-01-27 - Qian Qian (@Qubik65536)

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
    # IFM (round)
    Sensor("[OPT-101] Ox Fill", "AIN87", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[OPT 102] Ox Fill", "AIN95", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[NPT-201] N2 Fill", "AIN86", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[NPT-202] Pneumatics", "AIN94", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[OPT-301] Ox Tank", "AIN85", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-301] Fuel Tank", "AIN93", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[OPT-302] Ox Manifold", "AIN84", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    Sensor("[FPT-302] Fuel Manifold", "AIN92", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    # TDM (square)
    #Sensor("[OPT 101] Ox Fill (psi)", "AIN86", 10, Connection.SINGLE,
    #      LinearCalibration(1/100*3000/0.016, -0.004*3000/0.016, "psi"))

