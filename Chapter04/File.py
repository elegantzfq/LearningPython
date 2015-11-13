

f = open('file_test.txt', 'r')
lines = f.read().split()
print(lines)

for line in open('file_test.txt', 'r'):
    print(line)

