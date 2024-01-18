import sys

hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

data = ["Address           |  Data              | Command"]

with open(sys.argv[1].split("\\")[3].replace(".asm",".txt")) as f:
    lines = f.readlines()
for line in lines:
        if(line != '\n' and line!= ' outp | addr | data (base 2)\n'):
            binary = ''
            for digit in str(line.split('|')[1].replace(' ', '')):
                binary += hex_dict[digit]
            if(len(line.split('|')[2].split(";")[0].split(" ")) == 4):
               
                data.append("{:08d}".format(int(binary)) + " {:08d}".format(int(str(bin(int(binary,2) + 1)[2:])))+" | "+line.split('|')[2].replace('\n',"").replace(";","|"))
            else:
                data.append("{:08d}".format(int(binary)) +" "*9 + " | "+line.split('|')[2].replace('\n',"").replace(";","|"))
            


with open(sys.argv[1].split("\\")[3].replace(".asm",".txt"),'w') as f:

     for item in data:
          f.write(item+"\n")