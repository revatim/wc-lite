# Python
with open('corrupt_file.txt', 'wb') as f:
    f.write(b'\x80abc')