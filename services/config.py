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
    Sensor("[OPT 102] Ox Fill (psi)", "AIN87", 10, Connection.SINGLE,
          LinearCalibration(1/100*1450/0.016, -0.004*1450/0.016, "psi"))
    # TDM (square)
    Sensor("[OPT 101] Ox Fill (psi)", "AIN86", 10, Connection.SINGLE,
          LinearCalibration(1/100*3000/0.016, -0.004*3000/0.016, "psi"))

