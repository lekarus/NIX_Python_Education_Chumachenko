fWrite = open('test.txt', 'w')
fWrite.write('Hello, World!')
fWrite.close()
fOpen = open('test.txt', 'r')
print(fOpen.read())
fOpen.close()