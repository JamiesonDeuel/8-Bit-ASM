rom_size = 8192 

data = [0] * rom_size  

for address in range(rom_size):
    
    
    value = address & 0xff
    
    
    if(address & 0xF00 == 0):
        print(bin(address))
        data[address] = value



with open("output.bin", "wb") as f:
    f.write(bytes(data))
 

