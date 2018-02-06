
f = open('./result.txt', 'w')

f.write('hello\n')
f.write('nice to meet you')

f.close()

f = open('./result.txt', 'r')

print(f.read())
print(f.readline())
f.seek(0,0)
print(f.readline())
print(f.tell())
print(f.readline())

f.close()
