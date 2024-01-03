from pymem import *
from pymem.process import *
import time

offsets = [0x2A8, 0x90, 0x10, 0x50, 0x60, 0x50, 0x2C0]

pm = Pymem('1v1_LOL.exe')

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

            pm.write_int(GetPointer(gameModule, offsets), 100)

            time.sleep(0.1)

        except:

            pass