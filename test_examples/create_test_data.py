# Python
with open('corrupt_file.txt', 'wb') as f:
    f.write(b'\x80abc')
    
with open('byte_character.txt', 'w', encoding='utf-8') as f:
    f.write('€')