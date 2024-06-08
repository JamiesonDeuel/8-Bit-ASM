with open("address_content.bin", "wb") as bin_file:
    for i in range(256):
        bin_file.write(bytes([i]))
