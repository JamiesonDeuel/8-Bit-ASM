from intelhex import IntelHex
import sys
# ih = IntelHex(sys.argv[1])
print((IntelHex("D:\Documents\8-Bit-ASM\Display.hex")).todict())
# ih.tobinfile(sys.argv[1].replace(".hex",".bin"))
data = {}

for key in (IntelHex("D:\Documents\8-Bit-ASM\Display.hex")).todict():
    data[128+key] = IntelHex("D:\Documents\8-Bit-ASM\Display.hex").todict()[key]
   

print(data)
newHEX = IntelHex()
newHEX.fromdict(data)
newHEX.tofile("foo.hex", format='hex')