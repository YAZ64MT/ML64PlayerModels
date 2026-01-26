import sys
sys.path.append("./ml64modelpackagetopmm") # kludge

from os import SEEK_END
from shutil import rmtree
from ml64modelpackagetopmm.processzobjsbulk import process_zobjs_bulk
from pathlib import Path

def main() -> int:
    dest = Path("./processed_zobjs")
    rmtree(dest, True)

    process_zobjs_bulk(dest, Path("./Z64-CustomPlayerModels"))

    # for some reason this adult zobj is using the child header
    # let's manually fix that
    try:
        payapath = Path("./processed_zobjs", "Adult_Paya", "Paya.zobj")
        payadat = bytearray(payapath.read_bytes())
        payadat[0x500B] = 0
        payadat[0x500F] = 0x80
        payapath.write_bytes(payadat)
    except:
        pass

    return 0

if __name__ == "__main__":
    sys.exit(main())
