rom_size = 2048 

data = [0] * rom_size  

UCODE_Save = [0b00010011,0b00010001,0b00011111,0b00010111]
UCODE_Load = [0b01000011,0b00001111,0b00000111,0b00000111]
# end start_reset RI Set CE 'RO 'ES 'EO
# 7       6        5  4   3   2   1   0
for address in range(rom_size):
    
    setup = (address & 0b10000000000) >> 10
    byte_sel = (address & 0b00000001000) >> 3
    end   = (address & 0b00000000100) >> 2
    step  = (address & 0b00000000011)
    
    if(byte_sel):
        if(end):
            if(step == 2):
                UCODE_Load[1] = 0b10111101;   
        else:
            if(setup == 0 and step != 3):
            
                UCODE_Load[step] = 0b00000111
            
            elif (step == 3 and setup == 0):
                UCODE_Load[3]= 0b00010111
            else:
                UCODE_Load = [0b01000011,0b00001111,0b00000111,0b00000111]
        data[address] = UCODE_Load[step]
    else:
        if(end):
            
            
            UCODE_Save[2] = 0b11010111;   
        else:
            if(setup == 0 and step != 3):
            
                UCODE_Save[step] = 0b00000111
            
            elif (step == 3 and setup == 0):
                UCODE_Save[3]= 0b00010111
            else:
                
                UCODE_Save = [0b00010011,0b00010001,0b00011111,0b00010111]
        data[address] = UCODE_Save[step]
    
   
   
    
with open("output.bin", "wb") as f:
    f.write(bytes(data))
 

