fWrite = open('words.txt', 'a')
fWrite.write('\nHello, Everyone!')
fWrite.close()
fRead = open('words.txt', 'r')
for line in fRead:
    print(line, end='')
fRead.close()
