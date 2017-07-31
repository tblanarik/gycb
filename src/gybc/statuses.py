import gybc
import os

def texts():
    return open(os.path.join(gybc.GYBC_PATH, 'bin', 'archive.txt')).readlines()