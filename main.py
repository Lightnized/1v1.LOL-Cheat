from pymem import *
from pymem.process import *
import time

offsets = [0x2A8, 0x80, 0x10, 0x58, 0x60, 0x50, 0x2C0] # Offsets for inf ammo.
offsets2 = [0x2A8, 0x88, 0x10, 0x68, 0x60, 0x88, 0xC0] # Offsets for inf health.

pm = Pymem('1v1_LOL.exe')

code = """

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Successfully attached to process!", "Made By samfr._", 0)

"""

pm.inject_python_interpreter()
pm.inject_python_shellcode(code)

gameModule = module_from_name(pm.process_handle, 'mono-2.0-bdwgc.dll').lpBaseOfDll


def GetPointer(base, offsets):
    addr = pm.read_longlong(base+0x0072A1D8)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = pm.read_longlong(addr + offset)
    return addr + offsets[-1]

if __name__ == '__main__':

    while True:

        try:

            pm.write_int(GetPointer(gameModule, offsets), 1000)

            pm.write_int(GetPointer(gameModule, offsets2), 10000)

            time.sleep(0.001)

        except:

            pass
