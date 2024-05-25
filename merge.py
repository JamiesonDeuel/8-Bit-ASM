# Read the binary file
with open('output.bin', 'rb') as file:
    binary_data = file.read()

# Read the AT28C64B binary file
with open('AT28C64B.bin', 'rb') as file:
    AT28C64B = file.read()

# Create a mutable bytearray from AT28C64B to allow modifications
AT28C64B_data = bytearray(AT28C64B)

# Swap the content of output to AT28C64B at the same address
for index, byte in enumerate(binary_data):
    AT28C64B_data[index] = byte

# Write the updated data back to the AT28C64B binary file
with open("AT28C64B.bin", "wb") as file:
    file.write(AT28C64B_data)
